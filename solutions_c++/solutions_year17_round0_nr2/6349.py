#include<bits/stdc++.h>
using namespace std;
#define f(i,x,y) for(long long i = (x);i < (y);++i)
#define F(i,x,y) for(long long i = (x);i > (y);--i)

vector<long long> func(long long n)
 {
     vector<long long> vec;
     long long a = n;
    while(a != 0)
    {
        vec.push_back(a%10);
        a /= 10;
    }
    reverse(vec.begin(),vec.end());
    return vec;
 }


 vector<long long> main_func(long long n)
 {
     vector<long long> vec = func(n);
     if(vec.size() == 1)return vec;
     long long i = 0;
     long long sz = vec.size();
     while(i < sz)
     {
         long long s = i;
         while((i < (sz-1))&&(vec[i] == vec[i+1]))i++;
         long long e = i;
         if((e < (sz-1))&&(vec[e+1] < vec[e]))
         {
            vec[s] = vec[e]-1;
            f(i,(s+1),vec.size())vec[i] = 9;
         }
         i++;
     }
     return vec;
 }

int main()
{
int T;
cin >> T;
f(l,1,(T+1))
{
    string str = "";
    long long N;
    cin >> N;
    vector<long long> vec = main_func(N);
    long long k = 0;
    while((k < vec.size())&&(vec[k] == 0))k++;
    f(i,k,vec.size())str += (vec[i]+'0');
    cout <<"Case #"<<l<<": "<< str << endl;
}
return 0;
}