#include<bits/stdc++.h>
using namespace std;
#define f(i,x,y) for(long long i = (x);i < (y);++i)
#define F(i,x,y) for(long long i = (x);i > (y);--i)
 
typedef struct str
{
   string s;
   int st;   
}str;

int func(string &strin,int K)
{
    int max = (pow(2,strin.size()));
    int count = 0;
    queue< str > q;
     str val;
     val.s = strin;
     val.st = 0;
     q.push(val);
     while(count < 100000)
     {
         count++;
         int flag = 1;
         str cr = q.front();
         q.pop();
         string sr = cr.s;
         cout << sr  << " " << cr.st << endl;
         int n = sr.size();
         int steps = cr.st;
         f(i,0,n)
           if(sr[i] == '-'){flag = 0;break;}
        if(flag == 1)return steps;
        int i = 0,j = (K-1);
        while(j < n)
        {
            string vin = sr;
            str nw;
            nw.st = steps+1;
            f(k,i,(j+1))
            {
                if(vin[k] == '-')vin[k] = '+';
                else vin[k] = '-';
            }
            nw.s = vin;
            q.push(nw);
            j++;i++;
        }
     }
    return -1;
}


int main()
{
    int T;
    cin >> T;
    f(l,1,(T+1))
    {
       string str;
       int K;
       cin >> str;
       cin >> K;
       int ans = func(str,K);
       if(ans != -1)cout <<"Case #"<<l<<": "<< ans << endl;
       else cout <<"Case #"<<l<<": IMPOSSIBLE" << endl;
    }
}