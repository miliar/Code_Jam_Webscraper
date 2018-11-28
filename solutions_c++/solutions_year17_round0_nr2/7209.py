/*
	Be ashamed to die .. until you have Scored some Victory for Humanity
*/

#include <iostream>
#include <string>
#include <iomanip>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
#include <iterator>
#include <queue>
#include <fstream>
#include <stack>
#include <sstream>
#include <cstring>

using namespace std;


typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef map<string ,int> mpsi;



#define _OO (ll) -1e12
#define  OO (ll) 1e12
#define mem(arr,value) memset(arr,value,sizeof(arr))
#define pb push_back

// i,j+1 | i+1,j | i-1,j | i,j-1

int di[] = {1, -1, 0, 0};
int dj[] = {0, 0, 1, -1};

/*const int n = (int)1e6+1;
bool isPrime[n];
void Seive(){
	mem(isPrime, true);
	isPrime[0] = isPrime[1] = false;
	lpi(2,(int)1e6){
		if (isPrime[i]){
			for(int j=2*i;j<=(int)1e6;j+=i){
				isPrime[j] = false;
			}
		}
	}
}*/
string S;
bool good(){
	for(int i=0;i<S.size()-1;i++){
		if (S[i] > S[i+1])
			return false;
	}
	return true;
}

int main(){
	ifstream in("B-large.in", ios::in);
	ofstream out("out.txt", ios::out);
	 int n;
    string s;
    in>>n;
    for(int i=0;i<n;i++)
    {
        in>>s;
        int endd=s.length()-1;
        for(int j=0;j<endd;j++)
        {
            int first=j;
            bool wrong=0;
            for(int l=j+1;l<s.length();l++)
            {
                if(s[j]<s[l])
                {
                    break;
                }
                if(s[j]>s[l])
                {
                    wrong=1;
                    break;
                }
            }
            if(wrong)
            {
                s[j]=(char)((int)s[j]-1);
                for(++j;j<s.length();j++)
                {
                    s[j]='9';
                }
            }
        }
        for(int k=0;k<s.length();k++)
        {
            if(s[k]=='0')
            {
                s.erase(k,1);
            }
        }
        out<<"Case #"<<i+1<<": "<<s<<endl;
    }
return 0;
}