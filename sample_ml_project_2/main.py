from fastapi import FastAPI, responses
from fastapi.openapi.utils import get_openapi
from fastapi_health import health

from sample_ml_project_2.routes.router import router

__version__ = "0.0.2"

app = FastAPI(
    title="sample-ml-project-2 APIs",
    description="This is a template repository for Python projects that use Poetry for their dependency management.",
    version=__version__,
    docs_url="/docs",
    redoc_url="/redoc",
)


app = FastAPI()


# Default route redirects to docs
@app.get("/", include_in_schema=False)
async def root():
    return responses.RedirectResponse("/docs")


async def health_check():
    return {"status": "healthy"}


# Include routers
app.add_api_route("/health", health([health_check]), tags=["Management"], description="Management APIs")
app.include_router(router, prefix="/api/v1", tags=["Model Operations"])


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="sample-ml-project-2 APIs",
        description="This is a template repository for Python projects that use Poetry for their dependency management.",
        version=__version__,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


def main():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
