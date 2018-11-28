#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <array>

using namespace std;

int leftDistance(auto arr, int i, int n)
{
    int res = 0;
    for(int x = i - 1; x > 0; x--){
        if(arr[x])
        {
           break;
        }
        res++;
    }
    return res;
}
int rightDistance(auto arr, int i, int n)
{
    int res = 0;
    for(int x = i + 1; x < n - 1; x++){
        if(arr[x])
        {
           break;
        }
        res++;
    }
    return res;
}

int main()
{
    ifstream fin("small.in");
    ofstream fout("small.out");

    int t;
    fin >> t;
    for(int i = 0; i < t; i++)
    {
        int n, k;
        fin >> n >> k;
        n += 2;
        array<bool, 1500> stalls;
        stalls.fill(false);
        stalls[0] = stalls[n - 1] = true;

        int index = 0;
        int l = 0;
        int r = 0;

        if(n - 2 == k){
            fout << "Case #" << i + 1 << ": " << "0 0" << endl;
        }
        else{
            for(int x = 0; x < k; x++)
            {
                index = 0;
                l = 0;
                r = 0;
                for(int j = 1; j < n - 1; j++)
                {
                    if(stalls[j]) continue;
                    int left = leftDistance(stalls, j, n);
                    int right = rightDistance(stalls, j, n);

                    if(min(left, right) > min(l, r))
                    {
                        l = left;
                        r = right;
                        index = j;
                    }
                    else if(min(left, right) == min(l, r))
                    {
                        if(max(left, right) > max(l, r))
                        {
                            l = left;
                            r = right;
                            index = j;
                        }
                        else if(max(left, right) == max(l, r)) continue;
                    }


                }
                stalls[index] = true;
            }
            fout << "Case #" << i + 1 << ": " << max(l, r) << " " << min(l, r) << endl;
        }
    }


    return 0;
}
