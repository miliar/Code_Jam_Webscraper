#include <bits/stdc++.h>

using namespace std;
using ull = unsigned long long;
using ll = long long;
using ld = long double;
using D = double;
using ii = pair<int, int>;
using vi = vector<int>;
using vii = vector<ii>;

#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define makeunique(x) sort(all(x)), (x).resize(unique(all(x)) - (x).begin())
#define rep(i, x)  for(int i = 0; i < (x); i++)
#define rrep(i, x) for(int i = (x - 1); i >= 0; i--)
#define sqrt(x) sqrt(abs(x))
#define y1 y1_1234413
#define j1 j1_235
#define y0 y0_235
#define j0 j0_256
#define fi first
#define se second
#define re return
#define prev PREV
#define next NEXT
#define sz(x) ((int)x.size())

template<typename T> T sqr(T a) { re a * a; }
template<typename T> T gcd(T a, T b) { re b ? gcd(b, a % b) : a; }
template<typename T> T sgn(T a) { re a > 0 ? 1 : (a < 0 ? -1 : 0); }
template<typename T> T abs(T a) { re a > 0 ? a : -a; }

const int inf = 2*1e9;
const ld pi = acos((ld)-1);	
const int N = 2e5 + 10;
                                       
#define FILENAME ""
int n;

bool func(int x)
{   
 	string ss;
	while(x > 0)
		{ 
			ss += (char) '0' + x % 10;
			x/=10;
		}
	reverse(all(ss));
	for(int i = 1; i <sz(ss); i++)
		if(ss[i - 1] - '0' > ss[i] - '0') re false;
	re true;
}

int main()
{
    cin >> n;
    for(int j = 0; j < n; j++)
    {
        
    int a[100];
    string s;    
    cin >> s;
    int zz = 0;
	for(int i = 0; i < sz(s); i++)
		{
		 	zz *= 10;
			zz += s[i] - '0';

		}	

int ans = -1;

	for(int i = zz; i>=0; i--)
		{
		  if(func(i))
			{ans = i; break;}

		}		
	
	cout <<"Case #"<< j + 1 << ": "<< ans << endl;
}
 /*   

    int p = -1;
    for(int i = 0; i < sz(s); i++)
        a[i] = s[i] - '0';
    int t = 0;
    for(int i = 1; i < sz(s); i++)
        if(a[i] < a[i - 1])
            {
                t = 1; 
                p = i - 1;
                break;
            }
    if(t == 0) {cout << s << endl; continue;} 
    if(p == 0)
            {
                if(a[0] > 1) {
                    cout << a[0] - 1;
                    for(int i = 1; i < sz(s); i++)
                        cout << 9;
                            }
                else 
                    for(int i = 1; i < sz(s); i++)
                        cout << 9;
                cout << endl;        
                continue;        
            }  
            
        else
        {
            int z =  -1;
            for(int i = p - 1; i >= 0; i--)
                if(a[i] < a[p])
                    {z = i; break;}
            if(z > -1)
                {
                    for(int i = 0; i <= z; i++) 
                        cout << a[i];
                    for(int i = z + 1; i <= p; i++)
                        cout << a[p] - 1;
                    for(int i  = p + 1; i < sz(s); i++)
                        cout << 9;
                }
            else 
            {
                if(a[0] > 1)
                    {
                        for(int i = 0; i <= p; i++)
                            cout << a[p] - 1; 
                        for(int i = p + 1; i < sz(s); i++)
                            cout << 9;
                    }  
                else 
                    for(int i = 1; i < sz(s); i++)
                            cout << 9;
                           
            } 
            cout << endl;  
        }
    } */ 
    re 0;                 
}