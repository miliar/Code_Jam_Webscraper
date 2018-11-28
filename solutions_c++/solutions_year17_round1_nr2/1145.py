#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream ifs("B-small-attempt0.in");
    ofstream ofs("B-small-attempt0.out");

    int T;
    ifs >> T;


    for(int i=0; i<T; i++)
    {
        unsigned long long N, P;
        ifs >> N >> P;

        unsigned long long R[N];
        for(int j=0; j<N; j++)
        {
            ifs >> R[j];
        }

        unsigned long long Q[N][P];
        for(int j=0; j<N; j++)
        {
            for(int k=0; k<P; k++)
            {
                ifs >> Q[j][k];
            }
        }

        vector<unsigned long long> ratas;
        for(unsigned long long j=1; j<=1000000; j++)
        {
            bool valid = true;
            for(int k=0; k<N; k++)
            {
                bool oneValid = false;
                for(int l=0; l<P; l++)
                {
                    oneValid = oneValid || (R[k]*9*j<=Q[k][l]*10 && R[k]*11*j>=Q[k][l]*10);
                }
                valid = valid && oneValid;
            }
            if(valid)
            {
                ratas.push_back(j);
            }
        }

        int totalValidKits = 0;
        for(unsigned long long rata : ratas)
        {
            int validKits = 0;
            for(int j=0; j<N; j++)
            {
                int validPackages = 0;
                for(int k=0; k<P; k++)
                {
                    if(R[j]*9*rata<=Q[j][k]*10 && R[j]*11*rata>=Q[j][k]*10)
                    {
                        validPackages++;
                    }
                }

                if(j == 0)
                {
                    validKits = validPackages;
                }
                else
                {
                    validKits = min(validKits, validPackages);
                }
            }

            for(int j=0; j<N; j++)
            {
                int validPackages = 0;
                for(int k=0; k<P && validPackages<validKits; k++)
                {
                    if(R[j]*9*rata<=Q[j][k]*10 && R[j]*11*rata>=Q[j][k]*10)
                    {
                        Q[j][k] = 0;
                        validPackages++;
                    }
                }
            }

            totalValidKits += validKits;
        }

        ofs << "Case #" << i+1 << ": " << totalValidKits << endl;
    }
}
