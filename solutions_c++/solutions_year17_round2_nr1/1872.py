#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <iomanip>


void Input(unsigned int& T, std::istream& In = std::cin)
{
    In >> T;
}

void SolveOne(unsigned int Case, std::istream& In = std::cin, std::ostream& Out = std::cout)
{
    unsigned int D, N;
    std::vector< unsigned int > LstK, LstS;

    In >> D;
    In >> N;
    LstK.resize(N);
    LstS.resize(N);
    double MaxTime = 0;
    for (unsigned int i = 0 ; i < N ; i++)
    {
        In >> LstK[i];
        In >> LstS[i];
        if ((double)(D - LstK[i])/(double)LstS[i] > MaxTime)
        {
            MaxTime = (double)(D - LstK[i])/(double)LstS[i];
        }
    }

    Out.precision(6);
    Out.setf( std::ios::fixed, std:: ios::floatfield );
    Out << "Case #" << Case << ": " << (double)D / MaxTime << std::endl;
}

void Solve(unsigned int Index, std::ostream& Out = std::cout)
{

}


int main()
{
    unsigned int T;

    std::ifstream FileIn("A-large.in", std::ifstream::in);
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
