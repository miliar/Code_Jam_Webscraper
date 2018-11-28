#include <fstream>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <iomanip>
#include <queue>
#include <vector>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

typedef int INT;

#define int long long
#define double long double
int mod = 1e9+7;
int inf = 1e9;
vector<int> a;

string f(string x)
{
    string s = x;
    sort(s.begin(),s.end());
    
    if (s==x)
        return s;
    s = x;
    for (int i = s.size()-1; i>=0; i--)
    {
        int j = i-1;
        s[i] = '9';
        while(j > 0 && s[j] == '0')
        {
            s[j] = '9';
            j--;
        }
        s[j]-=1;
        string res = "";
        j = 0;
        while (s[j]=='0')
            j++;
        while (j<s.size())
            res+=s[j++];
        x = res;
        sort(x.begin(),x.end());
        if (x==res)
            return x;
    }
    return "0";
}
INT main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int T;
    cin >> T;
    for (int t = 0; t<T; t++)
    {
        
        string x;
        cin >> x;
 //       for (int i = 1; i<=1000; i++)
  //      {
  //          x = to_string(i);
   //         cout << x << " "<< f(x) << endl;
            cout << "Case #" << t+1 <<": " << f(x) << endl;
      //  }
    }
    return 0;
}
