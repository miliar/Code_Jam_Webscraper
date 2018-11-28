#include<bits/stdc++.h>
using namespace std;



int n, R, O, Y, G, B, V;
string ans;


// small

vector<pair<int, string>> arr(3);
string solve()
{
    sort(arr.rbegin(), arr.rend());
    string ans = "";
    
    for(int i = 0; i < arr[1].first; i++)
    {
        ans += arr[0].second;
        arr[0].first--;
        ans += arr[1].second;
        //arr[1].first--;
    }
    for(int i = 0; i < min(arr[0].first, arr[2].first); i++)
    {
        ans += arr[0].second;
        arr[0].first--;
        ans += arr[2].second;
        arr[2].first--;
    }
    if(arr[0].first)
    {
        return "IMPOSSIBLE";
    }
    else
    {
        for(int i = 0; i < min(arr[1].first, arr[2].first); i++)
        {
            ans.insert(i * 3 + 2, arr[2].second);
        }
    }
    return ans;
}


int main ()
{
    freopen("/Users/KhalidRamadan/Desktop/input.txt", "r", stdin);
    freopen("/Users/KhalidRamadan/Desktop/output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int T = 1; T <= t; T++)
    {
        ans = "";
        
        cin >> n >> R >> O >> Y >> G >> B >> V;
        arr[0] = {R, "R"};
        arr[1] = {Y, "Y"};
        arr[2] = {B, "B"};
        cout << "Case #" << T << ": ";
        cout << solve() << endl;
    }
}

