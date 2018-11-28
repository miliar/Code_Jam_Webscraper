#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <iomanip>
#include <algorithm>

const double PI = 3.141592653589793238462643383279502884;

typedef std::pair< double,double > MyPair;
bool comparator(const MyPair& l, const MyPair& r)
{
    return (l.first * l.second) < (r.first * r.second);
}


void SolveOne(unsigned int Case, std::istream& In = std::cin, std::ostream& Out = std::cout)
{
    unsigned int N, K;

    Out.precision(9);
    Out.setf(std::ios::fixed, std:: ios::floatfield );

    In >> N;
    In >> K;

    std::vector< MyPair > LstPan(N);
    for (unsigned int i = 0 ; i < N ; i++)
    {
        In >> LstPan[i].first;
        In >> LstPan[i].second;
    }

    sort(LstPan.begin(), LstPan.end(), comparator);

    double Sum = 0;
    double BestRadius = 0;
    for (int i = N - K ; i < N ; i++)
    {
        Sum += LstPan[i].first * LstPan[i].second;
        if (LstPan[i].first > BestRadius)
        {
            BestRadius = LstPan[i].first;
        }
    }
    Sum *= 2.;
    //Sum += BestRadius * BestRadius;

    double BestSum = Sum;
    double TotSum = Sum + BestRadius * BestRadius;
    for (int i = N - K - 1 ; i >= 0 ; i--)
    {
        for (unsigned int j = N - K ; j < N ; j++)
        {
            if (LstPan[i].first > BestRadius)
            {
                double NewSum = Sum + 2 * (LstPan[i].first * LstPan[i].second - LstPan[j].first * LstPan[j].second);
                if (NewSum + LstPan[i].first * LstPan[i].first > TotSum)
                {
                    BestSum = NewSum;
                    TotSum = NewSum + LstPan[i].first * LstPan[i].first;
                }
            }
        }
    }

    Out << "Case #" << Case << ": " << PI * TotSum << std::endl;
}

int main()
{
    unsigned int T;

    std::ifstream FileIn("A-large.in", std::ifstream::in);
    std::ofstream FileOut("out.out", std::ofstream::out);

    FileIn >> T;
    //std::cin >> T;

    for (unsigned int i = 0 ; i < T ; i++)
    {
        SolveOne(i + 1, FileIn, FileOut);
    }

    FileIn.close();
    FileOut.close();

    return 0;
}
