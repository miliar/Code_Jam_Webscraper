#include <iostream>
#include <fstream>

const unsigned int LTH_N = 18;


void Input(unsigned int& T, unsigned long long*& LstN, std::istream& In = std::cin)
{
    //std::ifstream FileIn("A-large.in");

    In >> T;

    LstN = new unsigned long long[T];
    for (unsigned int i = 0 ; i < T ; i++)
    {
        In >> LstN[i];
    }

    //FileIn.close();
}

bool IsSorted(char* NN, unsigned int& Index)
{
    char LastDigit = NN[0];

    for (unsigned int i = 1 ; i < LTH_N ; i++)
    {
        if (NN[i] < LastDigit)
        {
            while (NN[i] == 0)
            {
                i++;
                if (i >= LTH_N)
                {
                    Index = LTH_N - 1;
                    return false;
                }
            }
            Index = i;
            return false;
        }
        else
        {
            LastDigit = NN[i];
        }
    }
    return true;
}

void DecreaseNN(char* NN, unsigned int i)
{
    if (NN[i] != 0)
    {
        NN[i]--;
    }
    else
    {
        NN[i] = 9;
        DecreaseNN(NN, i - 1);
    }
}

void Solve(unsigned int Index, unsigned long long N, std::ostream& Out = std::cout)
{
    char* NN = new char[LTH_N];

    for (int i = LTH_N - 1 ; i >= 0 ; i--)
    {
        NN[i] = N % 10;
        N /= 10;
    }

    unsigned int BadIndex;
    while (!IsSorted(NN, BadIndex))
    {
        DecreaseNN(NN, BadIndex);
    }

    Out << "Case #" << Index << ": ";
    bool Zeros = true;
    for (unsigned int i = 0 ; i < LTH_N ; i++)
    {
        if (NN[i] != 0)
        {
            Zeros = false;
        }
        if (!Zeros)
        {
            Out << (int)NN[i];
        }
    }
    Out << std::endl;
}

int main()
{
    unsigned int T;
    unsigned long long* LstN;

    std::ifstream FileIn("B-small-attempt0.in", std::ifstream::in);
    std::ofstream FileOut("out.out", std::ofstream::out);

    Input(T, LstN, FileIn);

    for (unsigned int i = 0 ; i < T ; i++)
    {
        Solve(i + 1, LstN[i], FileOut);
    }

    FileIn.close();
    FileOut.close();
    delete[] LstN;
}

