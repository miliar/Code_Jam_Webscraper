#include<bits/stdc++.h>
using namespace std;
#define f(i,x,y) for(long long i = (x);i < (y);++i)
#define F(i,x,y) for(long long i = (x);i > (y);--i)



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
        int n = str.size();
        int i = 0;
        int flag = 0;
        while(i < n)
        {
            while((i < n)&&(str[i] == '+'))i++;
            int p = i;
            while((p < n)&&(str[p] == '-'))p++;
            if(i == n)break;
            //cout << str <<"<-"<< p << "<-" << i<< endl;
            if((n-i)<K){flag = -1;break;}
            else
            {
                f(j,0,K)
                {
                    if(str[i+j] == '+')str[i+j] = '-';
                    else str[i+j] = '+';
                }
            }
            //i = p;
            flag++;
        }
        if(flag != -1) cout <<"Case #"<<l<<": "<< flag << endl;
        else cout <<"Case #"<<l<<": IMPOSSIBLE" << endl;
    }
    return 0;
}