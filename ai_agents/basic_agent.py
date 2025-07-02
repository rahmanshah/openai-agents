from agents import Agent,Runner
from dotenv import load_dotenv,find_dotenv


load_dotenv(find_dotenv(), verbose=True)

agent = Agent(
    name="basic_agent",
    instructions="you are a helpful assistant",
    model="gpt-4o-mini"
)

def main():
    result = Runner.run_sync(agent, "Write a haiku about recursion in programming")
    print(result.final_output)


if __name__ == "__main__":
    main()
