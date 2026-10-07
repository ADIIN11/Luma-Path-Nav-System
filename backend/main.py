from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI application
app = FastAPI(
    title="Luma Path Nav System API",
    description="Backend for high-performance pathfinding, image segmentation, and graph extraction.",
    version="1.0.0"
)

# Configure CORS for local React/Vite development
# Update origins in production to your hosted frontend URL
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    """Health check endpoint to verify the API is running."""
    return {"status": "online", "message": "Luma Path Nav System API is running."}

# Note: Router includes for /upload and /ws will be added here in Phase 2 & 5.