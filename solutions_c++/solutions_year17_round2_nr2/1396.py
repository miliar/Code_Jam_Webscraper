#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstring>
#include <bitset>
#include <functional>
#include <map>

using namespace std;

typedef pair<int, int> pii;
typedef pair<pair<int, int>, pair<int, int>> piii;
typedef long long ll;
#define ff first.first
#define fs first.second
#define sf second.first
#define ss second.second

int t, n, r, o, y, g, b, v;
int arr[3];



int main(void)
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output-small-B.txt", "w", stdout);
    scanf("%d", &t);
    for(int x=1;x<=t;x++)
    {
        scanf("%d %d %d %d %d %d %d", &n, &arr[0], &o, &arr[1], &g, &arr[2], &v);
        int a = max({arr[0], arr[1], arr[2]});
        int b = arr[0]+arr[1]+arr[2] - a;
        if(a > b)
        {
            printf("Case #%d: IMPOSSIBLE\n", x);
            continue;
        }
        string result = "";
        int i = 0;
        if(a == arr[0])
        {
            while(n)
            {
                if(arr[0])
                {
                    result += 'R';
                    arr[0]--;
                    n--;
                }

                if(arr[1] >= arr[2] && arr[1] != 0)
                {
                    result += 'Y';
                    arr[1]--;
                    n--;
                }
                else if(arr[1] < arr[2] && arr[2] != 0)
                {
                    result += 'B';
                    arr[2]--;
                    n--;
                }
            }
        }
        else if(a == arr[1])
        {
            while(n)
            {
                if(arr[1])
                {
                    result += 'Y';
                    arr[1]--;
                    n--;
                }

                if(arr[0] >= arr[2] && arr[0] != 0)
                {
                    result += 'R';
                    arr[0]--;
                    n--;
                }
                else if(arr[0] < arr[2] && arr[2] != 0)
                {
                    result += 'B';
                    arr[2]--;
                    n--;
                }
            }
        }
        else if(a == arr[2])
        {
            while(n)
            {
                if(arr[2])
                {
                    result += 'B';
                    arr[2]--;
                    n--;
                }

                if(arr[0] >= arr[1] && arr[0] != 0)
                {
                    result += 'R';
                    arr[0]--;
                    n--;
                }
                else if(arr[0] < arr[1] && arr[1] != 0)
                {
                    result += 'Y';
                    arr[1]--;
                    n--;
                }
            }
        }
        cout << "Case #" << x << ": " << result <<'\n';
    }
}
