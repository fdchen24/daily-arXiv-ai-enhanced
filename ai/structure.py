from pydantic import BaseModel, Field, field_validator
import re

class Structure(BaseModel):
    tldr: str = Field(description="generate a too long; didn't read summary")
    task_background: str = Field(description="task context, inputs, outputs, and goal in 1-2 sentences, using only the supplied abstract")
    motivation: str = Field(description="specific limitations of existing work and why this paper is needed, distinct from the task background")
    method: str = Field(description="main approach and how its key steps address the identified problem")
    result: str = Field(description="brief experimental findings in 1-2 sentences, with benchmarks, comparisons, and numbers only when reported in the abstract; explicitly state when experimental results are not reported")
