#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <iomanip>


bool IsValidLstU(std::string const& LstU)
{
    for (unsigned int i = 1 ; i < LstU.size() ; i++)
    {
        if (LstU[i] == LstU[i - 1])
        {
            return false;
        }
    }
    if (LstU[0] == LstU[LstU.size() - 1])
    {
        return false;
    }

    return true;
}

void SolveOne(unsigned int Case, std::istream& In = std::cin, std::ostream& Out = std::cout)
{
    unsigned int N;
    unsigned int R, O, Y, G, B, V;

    In >> N;
    In >> R;
    In >> O;
    In >> Y;
    In >> G;
    In >> B;
    In >> V;

    std::string LstU;

    if (O == 0 && G == 0 && V == 0)
    {
        char CFirst;
        char CLast;
        if (R >= Y && R >= B)
        {
            CFirst = 'R';
            CLast = 'R';
            LstU += 'R';
            R--;
        }
        else if (Y >= R && Y >= B)
        {
            CFirst = 'Y';
            CLast = 'Y';
            LstU += 'Y';
            Y--;
        }
        else
        {
            CFirst = 'B';
            CLast = 'B';
            LstU += 'B';
            B--;
        }
        for (unsigned int i = 1 ; i < N ; i++)
        {
            if (i == N - 2 && CFirst == 'R' && R > 0)
            {
                LstU += 'R';
                CLast = 'R';
                R--;
            }
            else if (i == N - 2 && CFirst == 'Y' && Y > 0)
            {
                LstU += 'Y';
                CLast = 'Y';
                Y--;
            }
            else if (i == N - 2 && CFirst == 'B' && B > 0)
            {
                LstU += 'B';
                CLast = 'B';
                B--;
            }
            else
            {
                if (CLast == 'R')
                {
                    if (Y > 0 && Y >= B)
                    {
                        LstU += 'Y';
                        CLast = 'Y';
                        Y--;
                    }
                    else if (B > 0 && B >= Y)
                    {
                        LstU += 'B';
                        CLast = 'B';
                        B--;
                    }
                    else
                    {
                        LstU += 'R';
                        CLast = 'R';
                        R--;
                    }
                }
                else if (CLast == 'Y')
                {
                    if (B > 0 && B >= R)
                    {
                        LstU += 'B';
                        CLast = 'B';
                        B--;
                    }
                    else if (R > 0 && R >= B)
                    {
                        LstU += 'R';
                        CLast = 'R';
                        R--;
                    }
                    else
                    {
                        LstU += 'Y';
                        CLast = 'Y';
                        Y--;
                    }
                }
                else
                {
                    if (R > 0 && R >= Y)
                    {
                        LstU += 'R';
                        CLast = 'R';
                        R--;
                    }
                    else if (Y > 0 && Y >= R)
                    {
                        LstU += 'Y';
                        CLast = 'Y';
                        Y--;
                    }
                    else
                    {
                        LstU += 'B';
                        CLast = 'B';
                        B--;
                    }
                }
            }
        }

        Out << "Case #" << Case << ": ";

        if (!IsValidLstU(LstU))
        {
            Out << "IMPOSSIBLE " << std::endl;
        }
        else
        {
            Out << LstU << std::endl;
        }
    }
    else
    {
        Out << "Case #" << Case << ": ";

        if (!IsValidLstU(LstU))
        {
            Out << "IMPOSSIBLE" << std::endl;
        }
        else
        {
            Out << LstU << std::endl;
        }
    }
}

int main()
{
    unsigned int T;

    std::ifstream FileIn("B-small-attempt0.in", std::ifstream::in);
    std::ofstream FileOut("out.out", std::ofstream::out);

    FileIn >> T;

    for (unsigned int i = 0 ; i < T ; i++)
    {
        SolveOne(i + 1, FileIn, FileOut);
    }

    FileIn.close();
    FileOut.close();

    return 0;
}
