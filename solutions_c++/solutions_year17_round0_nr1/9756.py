
#include <cstdio>
#include <cstring>
#include <memory>
#include <utility>

using namespace std;

//USING_DEBUF_LEVEL0

#ifdef USING_DEBUF_LEVEL0
#define DebugLevel0(MSG, ...) printf(MSG, __VA_ARGS__)
#else
#define DebugLevel0(...)
#endif

//#define USING_DEBUF_LEVEL1

#ifdef USING_DEBUF_LEVEL1
#define DebugLevel1(MSG, ...) printf(MSG, __VA_ARGS__)
#else
#define DebugLevel1(...)
#endif

///////////////////////////////////////////////////
class Pancake
{
public: //TYPE MEMBER
	typedef shared_ptr<char> RowOfPancakes;
	typedef shared_ptr<Pancake> PancakePtr;
	class FlipPancakes;
	typedef shared_ptr<FlipPancakes> FlipPancakesPtr;
private: //MEMBER
	static RowOfPancakes ms_rowOfPancakes;
	size_t m_rowOfPancekesSize;
	size_t m_sizeFlipped;
	FlipPancakesPtr m_flipPancakes;
	FlipPancakesPtr m_flipPancakesMinimum;
public: //MEMBER
	Pancake();
	~Pancake();
	void Init();
	int Run();
	char * GetRowOfPancakes();
};

class Pancake::FlipPancakes
{
public:
	typedef char * PancakesInHand;
	typedef pair<char *, size_t> Block;
private:
	size_t m_sizeInHand;
	size_t m_sizeHappySide;
	PancakesInHand m_pancakesInHand;
public:
	static size_t ms_sizeDoFlipped;
	static void Reset();
	FlipPancakes(const size_t& size);
	FlipPancakes(const FlipPancakes & object);
	FlipPancakes(FlipPancakes * pointer);
	~FlipPancakes();
	bool IsHappy();
	bool IsNotHappy();
	size_t GetSizeHappySide();
	void Set(char * positionBlock);
	static size_t Flip(char * positionBlock, const size_t & sizeInHand, const size_t & sizeHappySide);
	void Flip();
	static Block GetLastBlockHappyStartFromLeft(char * positionBlock, const size_t & sizeInHand);
	Block GetLastBlockHappyStartFromLeft();
};

///////////////////////////////////////////////////
int main()
{
	size_t test;
	Pancake::PancakePtr pancake(0);
	int sucsess = fscanf(stdin, "%d", &test);
	if (sucsess)
	{
		for (size_t i = 0; i < test; ++i)
		{
			pancake = Pancake::PancakePtr(new Pancake());
			if (i != 0)
			{
				printf("\n");
			}
			printf("Case #%d: ", i + 1);
			int result = pancake->Run();
			DebugLevel1("%s", pancake->GetRowOfPancakes());
			pancake.reset();
		}
	}
	return 1;
}

Pancake::RowOfPancakes Pancake::ms_rowOfPancakes = RowOfPancakes(new char[1001], [](const char * p) {delete[] p; });

///////////////////////////////////////////////////
Pancake::Pancake():
	m_rowOfPancekesSize(0),
	m_sizeFlipped(0),
	m_flipPancakes(0)
{}

///////////////////////////////////////////////////
Pancake::~Pancake()
{}

///////////////////////////////////////////////////
void Pancake::Init()
{
	int sucsess = fscanf(stdin, "%s %d", ms_rowOfPancakes.get(), &m_sizeFlipped);
	if (sucsess)
	{
		m_rowOfPancekesSize = strlen(ms_rowOfPancakes.get());
		m_flipPancakes = FlipPancakesPtr(new FlipPancakes(m_sizeFlipped));
	}
}

///////////////////////////////////////////////////
int Pancake::Run()
{
	Init();
	size_t startIndex = 0;
	size_t index = 0;
	size_t circleSize = 0;
	bool isHappy = true;
	char * minimum = 0;
	size_t minimumSizeHappySide = 0;
	FlipPancakes::Reset();

	char * check = ms_rowOfPancakes.get();

	while (true)
	{
		DebugLevel0("\n Index : %d , check : %s, isHappy : %s, RESULT : ", index, check, (isHappy ? "true" : "false"));
		{ //CHECK TO END
			if ((m_rowOfPancekesSize - index) < m_sizeFlipped) //RESET
			{
				if (minimum)
				{
					DebugLevel0("\n Flip in End Circle");
					FlipPancakes::Flip(minimum, m_sizeFlipped, minimumSizeHappySide);
					minimum = 0;
				}

				index = startIndex;
				++circleSize;
				if (isHappy)
				{
					printf("%d", FlipPancakes::ms_sizeDoFlipped);
					return 1;
				}
				isHappy = true;
				continue;
			}
		}

		m_flipPancakes->Set((ms_rowOfPancakes.get() + index));

		if (m_flipPancakes->IsNotHappy())
		{
			m_flipPancakes->Flip();
			if (isHappy && (startIndex < index + m_sizeFlipped))
			{
				startIndex = index + m_sizeFlipped;
				DebugLevel0("\n IsNotHappy set startIndex : %d, %d", startIndex, isHappy);
			}
		}
		else if (m_flipPancakes->IsHappy())
		{
			if (isHappy && (startIndex < index + m_sizeFlipped))
			{
				startIndex = index + m_sizeFlipped;
				DebugLevel0("\n IsHappy set startIndex : %d %d", startIndex, isHappy);
			}
		}
		else
		{
			/**/
			FlipPancakes::Block shift;
			if (isHappy)
			{
				isHappy = false;
				shift = m_flipPancakes->GetLastBlockHappyStartFromLeft();
				DebugLevel0("\n Shift : %d", shift.second);
				if (m_rowOfPancekesSize - (index + shift.second) >= m_sizeFlipped)
				{
					if (shift.second > 0)
					{
						isHappy = true;
					}
					index += shift.second;
					continue;
				}
				else
				{
					printf("IMPOSSIBLE");
					return 0;
				}
				
			}
			else 
			{
				if (!minimum || m_flipPancakes->GetSizeHappySide() < minimumSizeHappySide)
				{
					minimum = (ms_rowOfPancakes.get() + index);
					minimumSizeHappySide = m_flipPancakes->GetSizeHappySide();
				}
			}
		}

		index += 1;
	}
}

///////////////////////////////////////////////////
char * Pancake::GetRowOfPancakes()
{
	return ms_rowOfPancakes.get();
}

///////////////////////////////////////////////////
size_t Pancake::FlipPancakes::ms_sizeDoFlipped = 0;

///////////////////////////////////////////////////
Pancake::FlipPancakes::FlipPancakes(const size_t& size) :
	m_sizeInHand(size),
	m_sizeHappySide(0),
	m_pancakesInHand(0)
{}

///////////////////////////////////////////////////
Pancake::FlipPancakes::FlipPancakes(const Pancake::FlipPancakes & object) :
	m_sizeInHand(object.m_sizeInHand),
	m_sizeHappySide(object.m_sizeHappySide),
	m_pancakesInHand(object.m_pancakesInHand)
{}

///////////////////////////////////////////////////
Pancake::FlipPancakes::FlipPancakes(Pancake::FlipPancakes * pointer) :
	m_sizeInHand(pointer->m_sizeInHand),
	m_sizeHappySide(pointer->m_sizeHappySide),
	m_pancakesInHand(pointer->m_pancakesInHand)
{}

///////////////////////////////////////////////////
Pancake::FlipPancakes::~FlipPancakes()
{}

///////////////////////////////////////////////////
void Pancake::FlipPancakes::Reset()
{
	ms_sizeDoFlipped = 0;
}

///////////////////////////////////////////////////
bool Pancake::FlipPancakes::IsHappy()
{
	return m_sizeInHand == m_sizeHappySide;
}

///////////////////////////////////////////////////
bool Pancake::FlipPancakes::IsNotHappy()
{
	return m_sizeHappySide == 0;
}

///////////////////////////////////////////////////
size_t Pancake::FlipPancakes::GetSizeHappySide()
{
	return m_sizeHappySide;
}

///////////////////////////////////////////////////
void Pancake::FlipPancakes::Set(char * positionBlock)
{
	m_pancakesInHand = positionBlock;
	m_sizeHappySide = 0;
	for (size_t i = 0; i < m_sizeInHand; ++i)
	{
		if (*(m_pancakesInHand + i) == '+')
		{
			++m_sizeHappySide;
		}
	}
}

///////////////////////////////////////////////////
size_t Pancake::FlipPancakes::Flip(char * positionBlock, const size_t & sizeInHand, const size_t & sizeHappySide)
{
	DebugLevel0("\n [%s]", positionBlock);
	for (size_t i = 0; i < sizeInHand; ++i)
	{
		if (*(positionBlock + i) == '+')
		{
			*(positionBlock + i) = '-';
		}
		else
		{
			*(positionBlock + i) = '+';
		}
	}
	DebugLevel0("->[%s]", positionBlock);
	++ms_sizeDoFlipped;
	return sizeInHand - sizeHappySide;
}

///////////////////////////////////////////////////
void Pancake::FlipPancakes::Flip()
{
	m_sizeHappySide = Flip(m_pancakesInHand, m_sizeInHand, m_sizeHappySide);
}

///////////////////////////////////////////////////
Pancake::FlipPancakes::Block 
Pancake::FlipPancakes::GetLastBlockHappyStartFromLeft(char * positionBlock, const size_t & sizeInHand)
{
	for (size_t i = 0; i < sizeInHand; ++i)
	{
		if (*(positionBlock + i) == '-')
		{
			return Block((positionBlock + i), i);
		}
	}
	return Block(positionBlock - (sizeInHand - 1), (sizeInHand - 1));
}

///////////////////////////////////////////////////
Pancake::FlipPancakes::Block
Pancake::FlipPancakes::GetLastBlockHappyStartFromLeft()
{
	return GetLastBlockHappyStartFromLeft(m_pancakesInHand, m_sizeInHand);
}