#include <iostream>
#include <fstream>
#include <vector>
#include <stack>

using namespace std;

pair<int,int> getResult(int N, int K);
void getLeftRight(uint64_t N, uint64_t& left, uint64_t& right);

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int T;

    fin >> T;

    for (int t = 0; t < T; t++)
    {
        uint64_t N;
        uint64_t K;
        fin >> N >> K;

        uint64_t left = 0;
        uint64_t right = 0;

        uint64_t N1 = N;
        uint64_t N2 = 0;
        uint64_t k1 = 1;
        uint64_t k2 = 0;
        while (K > 0)
        {
            uint64_t newN1 = 0;
            uint64_t newN2 = 0;
            uint64_t newk1 = 0;
            uint64_t newk2 = 0;
            if (k2 > 0 && N2 > 0)
            {
                getLeftRight(N2, left, right);
                if (left != right)
                {
                    newN1 = left;
                    newk1 = k2;
                    newN2 = right;
                    newk2 = k2;
                } else {
                    newN2 = right;
                    newk2 += k2 * 2;
                }
                if (k2 >= K)
                    break;
                K -= k2;

            }
            if (k1 > 0 && N1 > 0)
            {
                getLeftRight(N1, left, right);
                if (left != right)
                {
                    newN1 = left;
                    newk1 += k1;
                    newN2 = right;
                    newk2 += k1;
                } else {
                    newN1 = left;
                    newk1 += k1 * 2;
                }
                if (k1 >= K)
                    break;
                K -= k1;
            }
            N1 = newN1;
            N2 = newN2;
            k1 = newk1;
            k2 = newk2;
        }

        fout << "Case #" << (t+1) << ": " << right << " " << left << endl;
    }

    return 0;
}

void getLeftRight(uint64_t N, uint64_t& left, uint64_t& right)
{
    left = N / 2;
    right = N / 2;
    if (N % 2 == 0)
        left --;
}

// bruteforce algorithm
pair<int,int> getResult(int N, int K)
{
    std::string str(N, '0');
    int MaxLeft = -1, MaxRight = -1;
    for (auto k = 0; k < K; k++)
    {
        int bestPlace = 0;
        MaxLeft = -1;
        MaxRight = -1;
        for (auto i = 0; i < N; i++)
        {
            if (str[i] == '0')
            {
                int l, r;
                for (l = i; l >= 0; l--)
                    if (str[l] == '1')
                        break;

                for (r = i; r < N; r++)
                    if (str[r] == '1')
                        break;

                auto left = i - l - 1;
                auto right = r - i - 1;

                if (min(MaxLeft, MaxRight) < min (left, right))
                {
                    bestPlace = i;
                    MaxLeft = left;
                    MaxRight = right;
                }
                if (min(MaxLeft, MaxRight) == min(left, right))
                {
                    if (max(MaxLeft, MaxRight) < max(left, right))
                    {
                        bestPlace = i;
                        MaxLeft = left;
                        MaxRight = right;
                    }
                }

            }
        }

        str[bestPlace] = '1';
    }

    return { MaxLeft, MaxRight };
};