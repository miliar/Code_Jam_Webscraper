#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int k = 0; k < T; k++)
    {
        int N, K;
        cin >> N >> K;
        int max1, max2;
        bool A[1000];
        int LS[1000];
        int RS[1000];
        int mini[1000];
        int maxi[1000];
        int i, j;
        cout << "Case #" << k+1 << ": ";
        if (N == K)
            cout << "0 0";
        else
        {
            for (i = 0; i < N; i++)
            {
                A[i] = false;
                LS[i] = RS[i] = 0;
            }
            for (int l = 0; l < K; l++)
            {
                int tmp = 0;
                int tmp2 = 0;
                for (i = 0, j = N-1; i < N; i++, j--)
                {
                    if (A[i])
                    {
                        tmp = 0;
                    }
                    else
                    {
                        LS[i] = tmp;
                        tmp++;
                    }
                    if (A[j])
                    {
                        tmp2 = 0;
                    }
                    else
                    {
                        RS[j] = tmp2;
                        tmp2++;
                    }
                }
                max1 = -1;
                int index1 = 0;
                max2 = -1;
                int index2 = 0;
                bool maisdeum1 = false;
                bool maisdeum2 = false;
                for (i = 0; i < N; i++)
                {
                    if (!A[i])
                    {
                        mini[i] = min(LS[i],RS[i]);
                        maxi[i] = max(LS[i],RS[i]);
                        if (mini[i] >= max1)
                        {
                            if (mini[i] == max1)
                            {
                                maisdeum1 = true;
                            }
                            else
                            {
                                max1 = mini[i];
                                maisdeum1 = false;
                                index1 = i;
                            }
                        }
                    }
                    else
                    {
                        mini[i] = -1;
                        maxi[i] = -1;
                    }
                }
                for (i = 0; i < N; i++)
                {
                    if (mini[i] == max1)
                    {
                        if (maxi[i] >= max2)
                        {
                            if (maxi[i] == max2)
                            {
                                maisdeum2 = true;
                            }
                            else
                            {
                                max2 = maxi[i];
                                maisdeum2 = false;
                                index2 = i;
                            }
                        }
                    }
                }
                if (!maisdeum1)
                {
                    A[index1] = true;
                }
                else if (!maisdeum2)
                {
                    A[index2] = true;
                }
                else
                {
                    for (i = 0; i < N; i++)
                    {
                        if (maxi[i] == max2 && mini[i] == max1)
                        {
                            A[i] = true;
                            break;
                        }
                    }
                }
            }
            cout << max2 << " " << max1;
        }
        cout << endl;
    }
    return 0;
}
