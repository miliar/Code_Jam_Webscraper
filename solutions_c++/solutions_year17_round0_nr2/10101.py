#include <cstdio>
#include <memory>

using namespace std;

//#define USING_DEBUG_LEVEL_0

#ifdef USING_DEBUG_LEVEL_0
#define DebugLevel0(MSG, ...) printf(MSG, __VA_ARGS__);
#else
#define DebugLevel0(...)
#endif

class Module
{
public:
	typedef shared_ptr<Module> ModulePtr;
protected:
	Module();
public:
	virtual ~Module() {};
	virtual void Init() = 0;
	virtual void Run() = 0;
	virtual void Print() = 0;
};

template <typename MODULE>
class Test :
	public Module
{
private:
	ModulePtr m_module;
	size_t m_size;
	size_t m_index;
public:
	Test();
	~Test();
	void Init();
	void Run();
	void Print();
};

class TidyNumbers :
	public Module
{
public:
	typedef unsigned long long NumberPrimitive;
	class Number;
	typedef shared_ptr<Number> NumberPtr;
private:
	NumberPrimitive m_numberPrimitive;
	size_t m_count;
	NumberPtr m_number, m_numberMaster;
public:
	TidyNumbers();
	~TidyNumbers();
	void Init();
	void Run();
	void Print();
};

class TidyNumbers::Number
{
public:
	typedef TidyNumbers::NumberPrimitive NumberPrimitive;
	typedef shared_ptr<char> RowOfNumber;
private:
	RowOfNumber m_rowOfNumber;
	size_t m_rowOfNumberSize;
	
	static void CastToNumber(Number * pointer, const NumberPrimitive& number);
	static void Increment(Number * pointer, size_t index = 0);
	static void Decrement(Number * pointer, size_t index = 0, bool carry = false);
public:
	static Number Copy(Number * pointer);
	static size_t CountDigitNumber(const NumberPrimitive& number);
	static bool IsTidyNumbers(Number * pointer);
	Number();
	Number(const NumberPrimitive& number);
	Number(const Number& number);
	Number(Number * pointer);
	~Number();
	void Print();
	Number operator =(const size_t& number);
	Number& operator ++();
	Number operator ++(int);
	Number& operator --();
	Number operator --(int);
	bool operator <(Number& number);
	bool operator >(Number& number);
	bool operator <=(Number & number);
	bool operator >=(Number & number);
	bool operator ==(Number & number);
	bool operator !=(Number & number);
};

typedef Module::ModulePtr ModulePtr;

//////////////////////////////////////////////////////
int main()
{
	ModulePtr test = ModulePtr(new Test<TidyNumbers>());
	test->Init();
	test->Run();
	return 1;
}

//////////////////////////////////////////////////////
Module::Module()
{}

//////////////////////////////////////////////////////
template <typename MODULE>
Test<MODULE>::Test() :
	m_size(0),
	m_index(0)
{}

//////////////////////////////////////////////////////
template <typename MODULE>
Test<MODULE>::~Test()
{}

//////////////////////////////////////////////////////
template <typename MODULE>
void Test<MODULE>::Init()
{
	int sucess = fscanf(stdin, "%d", &m_size);
}

//////////////////////////////////////////////////////
template <typename MODULE>
void Test<MODULE>::Run()
{
	for (m_index = 0; m_index < m_size; ++m_index)
	{
		DebugLevel0("Index : %d", m_index);
		m_module = ModulePtr(new MODULE());
		m_module->Init();
		m_module->Run();
		DebugLevel0("\nResult: ");
		Print();
		m_module->Print();
		DebugLevel0("\n");
	}
}

//////////////////////////////////////////////////////
template <typename MODULE>
void Test<MODULE>::Print()
{
	if (m_index > 0)
	{
		fprintf(stdout, "\n");
	}
	fprintf(stdout, "Case #%d: ", m_index + 1);
}

//////////////////////////////////////////////////////
TidyNumbers::TidyNumbers() :
	m_numberPrimitive(0),
	m_count(0)
{}

//////////////////////////////////////////////////////
TidyNumbers::~TidyNumbers()
{}

//////////////////////////////////////////////////////
void TidyNumbers::Init()
{
	int sucess = fscanf(stdin, "%llu", &m_numberPrimitive);
	DebugLevel0("Number : %llu", m_numberPrimitive);
	m_number = NumberPtr(new Number(m_numberPrimitive));
	m_numberMaster = NumberPtr(new Number(m_numberPrimitive));
}

//////////////////////////////////////////////////////
void TidyNumbers::Run()
{
	
#ifdef USING_DEBUG_LEVEL_0
	fprintf(stdout, "\nTEST : ");
	Number number(m_numberPrimitive);
	fprintf(stdout, "\n Result : ");
	number.Print();

	/*
	fprintf(stdout, "\n Increment : ");
	for (size_t i = 0; i < 1000; ++i)
	{
		number.Print();

		++number;
		fprintf(stdout, "\n");
	}
	*/
#endif
	//Number inc = Number();
	//Number max = Number(1000);
	/*
	size_t i = 0;
	for (; inc <= number; ++inc, ++i)
	{
		inc.Print();
		fprintf(stdout, "\n");
	}
	fprintf(stdout, "\n Result : %d",i);
	*/
	//Number dec = Number();
	if (!Number::IsTidyNumbers(m_number.get()))
	{
		--(*m_number.get());
		Number copy = Number::Copy(m_number.get());
		while (true)
		{
			++copy;
			if (copy <= (*m_numberMaster.get()))
			{
				++(*m_number.get());
			}
			else
			{
				break;
			}
		}
	}
	
}

//////////////////////////////////////////////////////
void TidyNumbers::Print()
{
	//fprintf(stdout, "%d: ", m_count);
	//fprintf(stdout, "%llu -> ", m_numberPrimitive);
	m_number->Print();
}

//////////////////////////////////////////////////////
bool TidyNumbers::Number::IsTidyNumbers(Number * pointer)
{
	char before = 0;
	for (size_t i = pointer->m_rowOfNumberSize; i > 0; --i)
	{
		if (i == pointer->m_rowOfNumberSize)
		{
			before = (pointer->m_rowOfNumber.get())[i - 1];
			continue;
		}
		if (before > (pointer->m_rowOfNumber.get())[i - 1])
		{
			return false;
		}
		before = (pointer->m_rowOfNumber.get())[i - 1];
	}
	return true;
}

//////////////////////////////////////////////////////
void TidyNumbers::Number::CastToNumber(Number * pointer, const NumberPrimitive& number)
{
	if (pointer)
	{
		NumberPrimitive copy = number;
		if (pointer->m_rowOfNumber)
		{
			pointer->m_rowOfNumber.reset();
			pointer->m_rowOfNumberSize = 0;
		} 
		pointer->m_rowOfNumber = RowOfNumber(new char[20], [](char * pointer) {delete[] pointer; });
		bool first = true;

		while (first || copy != 0)
		{
			first = false;
			NumberPrimitive shift = NumberPrimitive(copy / 10LLU);
			NumberPrimitive shiftRight = NumberPrimitive(shift * 10LLU);
			NumberPrimitive lastDigit = copy - shiftRight;
			DebugLevel0("\n lastDigit : %llu", lastDigit);
			char check = 48 + (char)lastDigit;
			(pointer->m_rowOfNumber.get())[pointer->m_rowOfNumberSize++] = 48 + (char)lastDigit;
			(pointer->m_rowOfNumber.get())[pointer->m_rowOfNumberSize] = 0;
			copy = shift;
		}
	}
}

//////////////////////////////////////////////////////
void TidyNumbers::Number::Increment(Number * pointer, size_t index)
{
	char * check = pointer->m_rowOfNumber.get();
	if (index >= pointer->m_rowOfNumberSize)
	{
		return;
	}
	if ((pointer->m_rowOfNumber.get())[index] == '9')
	{
		if (index + 1 == pointer->m_rowOfNumberSize)
		{
			(pointer->m_rowOfNumber.get())[index] = '1';
			(pointer->m_rowOfNumber.get())[pointer->m_rowOfNumberSize] = '1';
			(pointer->m_rowOfNumber.get())[++pointer->m_rowOfNumberSize] = 0;
			return;
		}
		Increment(pointer, index + 1);
		(pointer->m_rowOfNumber.get())[index] = (pointer->m_rowOfNumber.get())[index + 1];
	}
	else
	{
		(pointer->m_rowOfNumber.get())[index] += 1;
	}
}

//////////////////////////////////////////////////////
void TidyNumbers::Number::Decrement(Number * pointer, size_t index, bool carry)
{
	if (index >= pointer->m_rowOfNumberSize)
	{
		return;
	}

	if ((index + 1) < pointer->m_rowOfNumberSize)
	{
		if ((pointer->m_rowOfNumber.get())[index + 1] >= (pointer->m_rowOfNumber.get())[index])
		{
			if (index == 0)
			{
				(pointer->m_rowOfNumber.get())[index] = '9';
			}
			else 
			{
				(pointer->m_rowOfNumber.get())[index] = (pointer->m_rowOfNumber.get())[index - 1];
			}
			
			Decrement(pointer, index + 1, true);
		}
		else
		{
			if (carry)
			{
				if ((pointer->m_rowOfNumber.get())[index] == '0')
				{
					Decrement(pointer, index + 1, carry);
					if (index == 0)
					{
						(pointer->m_rowOfNumber.get())[index] = '9';
					}
					else
					{
						(pointer->m_rowOfNumber.get())[index] = (pointer->m_rowOfNumber.get())[index - 1];
					}
					
				}
				else
				{
					(pointer->m_rowOfNumber.get())[index] -= 1;
				}
			}
			else
			{
				Decrement(pointer, index + 1);
			}
			
			/*
			if ((pointer->m_rowOfNumber.get())[index + 1] >= (pointer->m_rowOfNumber.get())[index])
			{
				(pointer->m_rowOfNumber.get())[index] = '9';
			}
			*/
		}
	} 
	else
	{
		if (carry)
		{
			(pointer->m_rowOfNumber.get())[index] -= 1;
			if ((index + 1) >= pointer->m_rowOfNumberSize && (pointer->m_rowOfNumber.get())[index] == '0')
			{
				(pointer->m_rowOfNumber.get())[index] = 0;
				--pointer->m_rowOfNumberSize;
			}
		}
	}
}

//////////////////////////////////////////////////////
TidyNumbers::Number TidyNumbers::Number::Copy(Number * pointer)
{
	Number copy;
	copy.m_rowOfNumber = RowOfNumber(new char[20], [](char * pointer) {delete[] pointer; });
	memcpy(copy.m_rowOfNumber.get(), pointer->m_rowOfNumber.get(), 20);
	copy.m_rowOfNumberSize = pointer->m_rowOfNumberSize;
	return copy;
}

//////////////////////////////////////////////////////
size_t TidyNumbers::Number::CountDigitNumber(const NumberPrimitive& number)
{
	return 0;
}

//////////////////////////////////////////////////////
TidyNumbers::Number::Number() :
	m_rowOfNumber(0),
	m_rowOfNumberSize(0)
{
	CastToNumber(this, 0);
}

//////////////////////////////////////////////////////
TidyNumbers::Number::Number(const NumberPrimitive& number) :
	m_rowOfNumber(0),
	m_rowOfNumberSize(0)
{
	CastToNumber(this, number);
}

//////////////////////////////////////////////////////
TidyNumbers::Number::Number(const Number& number) :
	m_rowOfNumber(number.m_rowOfNumber),
	m_rowOfNumberSize(number.m_rowOfNumberSize)
{}

//////////////////////////////////////////////////////
TidyNumbers::Number::Number(Number * pointer) :
	m_rowOfNumber(pointer->m_rowOfNumber),
	m_rowOfNumberSize(pointer->m_rowOfNumberSize)
{}

//////////////////////////////////////////////////////
TidyNumbers::Number::~Number()
{}

//////////////////////////////////////////////////////
void TidyNumbers::Number::Print()
{
#ifdef USING_DEBUG_LEVEL_0
	fprintf(stdout, "[");
#endif
	for (size_t i = m_rowOfNumberSize; i > 0; --i)
	{
#ifdef USING_DEBUG_LEVEL_0
		if (i != m_rowOfNumberSize)
		{
			fprintf(stdout, ", ");
		}
#endif
		fprintf(stdout, "%c", (m_rowOfNumber.get())[i - 1]);
	}
#ifdef USING_DEBUG_LEVEL_0
	fprintf(stdout, "]");
#endif
}

//////////////////////////////////////////////////////
TidyNumbers::Number TidyNumbers::Number::operator =(const size_t& number)
{
	return Number(number);
}

//////////////////////////////////////////////////////
TidyNumbers::Number& TidyNumbers::Number::operator ++()
{
	Increment(this);
	return *this;
}

//////////////////////////////////////////////////////
TidyNumbers::Number TidyNumbers::Number::operator ++(int)
{
	Number ret(this);
	Increment(&ret);
	return ret;
}

//////////////////////////////////////////////////////
TidyNumbers::Number& TidyNumbers::Number::operator --()
{
	Decrement(this);
	return *this;
}

//////////////////////////////////////////////////////
TidyNumbers::Number TidyNumbers::Number::operator --(int)
{
	Number ret(this);
	Decrement(&ret);
	return ret;
}

//////////////////////////////////////////////////////
bool TidyNumbers::Number::operator <(Number& number)
{
	if (m_rowOfNumberSize != number.m_rowOfNumberSize)
	{
		return m_rowOfNumberSize < number.m_rowOfNumberSize;
	}
	for (size_t i = m_rowOfNumberSize; i > 0; --i)
	{
		if ((m_rowOfNumber.get())[i - 1] != (number.m_rowOfNumber.get())[i - 1])
		{
			return (m_rowOfNumber.get())[i - 1] < (number.m_rowOfNumber.get())[i - 1];
		}
	}
	return false;
}

//////////////////////////////////////////////////////
bool TidyNumbers::Number::operator >(Number& number)
{
	if (m_rowOfNumberSize != number.m_rowOfNumberSize)
	{
		return m_rowOfNumberSize > number.m_rowOfNumberSize;
	}
	for (size_t i = m_rowOfNumberSize; i > 0; --i)
	{
		if ((m_rowOfNumber.get())[i - 1] != (number.m_rowOfNumber.get())[i - 1])
		{
			return (m_rowOfNumber.get())[i - 1] > (number.m_rowOfNumber.get())[i - 1];
		}
	}
	return false;
}

//////////////////////////////////////////////////////
bool TidyNumbers::Number::operator <=(Number & number)
{
	if (m_rowOfNumberSize != number.m_rowOfNumberSize)
	{
		return m_rowOfNumberSize < number.m_rowOfNumberSize;
	}
	for (size_t i = m_rowOfNumberSize; i > 0; --i)
	{
		if ((m_rowOfNumber.get())[i - 1] != (number.m_rowOfNumber.get())[i - 1])
		{
			return (m_rowOfNumber.get())[i - 1] < (number.m_rowOfNumber.get())[i - 1];
		}
	}
	return true;
}

//////////////////////////////////////////////////////
bool TidyNumbers::Number::operator >=(Number & number)
{
	if (m_rowOfNumberSize != number.m_rowOfNumberSize)
	{
		return m_rowOfNumberSize > number.m_rowOfNumberSize;
	}
	for (size_t i = m_rowOfNumberSize; i > 0; --i)
	{
		if ((m_rowOfNumber.get())[i - 1] != (number.m_rowOfNumber.get())[i - 1])
		{
			return (m_rowOfNumber.get())[i - 1] > (number.m_rowOfNumber.get())[i - 1];
		}
	}
	return true;
}

//////////////////////////////////////////////////////
bool TidyNumbers::Number::operator ==(Number & number)
{
	if (m_rowOfNumberSize != number.m_rowOfNumberSize)
	{
		return false;
	}
	for (size_t i = m_rowOfNumberSize; i > 0; --i)
	{
		if ((m_rowOfNumber.get())[i - 1] != (number.m_rowOfNumber.get())[i - 1])
		{
			return false;
		}
	}
	return true;
}

//////////////////////////////////////////////////////
bool TidyNumbers::Number::operator !=(Number & number)
{
	return !(operator ==(number));
}