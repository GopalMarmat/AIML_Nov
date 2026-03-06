from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Preformatted
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors

# File name
file_path = "Generative_AI_Complete_Notes.pdf"
doc = SimpleDocTemplate(file_path, pagesize=letter)

# Code-style formatting
code_style = ParagraphStyle(
    name='CodeStyle',
    fontName='Courier',
    fontSize=9,
    leading=12,
    textColor=colors.black
)

content = """
GENERATIVE AI COMPLETE NOTES

1. Generative AI Definition
Generative AI is a type of Artificial Intelligence that creates new content such as text, images, code, music, or videos.
It learns patterns from large datasets and generates new similar content.

2. Prompt Engineering
Prompt Engineering is designing effective instructions to get better outputs from AI models.

Types:
- Zero-shot Prompting
- One-shot Prompting
- Few-shot Prompting
- Chain-of-Thought Prompting
- Role-based Prompting

Sample Python Code:
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful teacher."},
        {"role": "user", "content": "Explain gravity simply."}
    ]
)

3. Fine-Tuning Methods
Fine-tuning means training a pre-trained model on custom data.

Types:
- Full Fine-Tuning
- LoRA (Low Rank Adaptation)
- PEFT
- Instruction Fine-Tuning

Sample LoRA Code:
from transformers import AutoModelForCausalLM
from peft import LoraConfig, get_peft_model

model = AutoModelForCausalLM.from_pretrained("gpt2")
config = LoraConfig(r=16, lora_alpha=32)
model = get_peft_model(model, config)

4. RAG (Retrieval-Augmented Generation)
RAG retrieves relevant documents and sends them to LLM to generate grounded answers.

Architecture:
User Query → Embeddings → Vector DB → Retrieve Docs → LLM → Final Answer

5. LangChain
LangChain is a framework for building LLM applications by combining models, memory, tools, and vector databases.

6. Evaluation Metrics
Common Metrics:
- BLEU
- ROUGE
- Perplexity
- BERTScore
- Human Evaluation

BLEU Example:
from nltk.translate.bleu_score import sentence_bleu
reference = [["the", "cat", "is", "on", "the", "mat"]]
candidate = ["the", "cat", "sat", "on", "the", "mat"]
score = sentence_bleu(reference, candidate)

7. Hallucination Control
Hallucination happens when AI generates incorrect information.

Control Methods:
- Use RAG
- Grounding data
- Low temperature
- Validation pipeline

8. Agentic AI
Agentic AI systems can plan, take actions, use tools, and work toward goals autonomously.

9. MCP (Model Context Protocol)
MCP allows structured communication between AI models and external tools or data sources.

FINAL SUMMARY

Generative AI – Creates new content
Prompt Engineering – Improves instructions
Fine-tuning – Customizes models
RAG – Reduces hallucination
LangChain – Builds LLM applications
Evaluation – Measures performance
Hallucination Control – Improves reliability
Agentic AI – Autonomous systems
MCP – Structured tool communication
"""

elements = [Preformatted(content, code_style)]
doc.build(elements)

print("PDF generated successfully:", file_path)