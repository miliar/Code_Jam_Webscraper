#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <sstream>
#include <string>
#include <math.h>
#include <queue>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define RO(i,b,a) for (int i = (b); i >= (a); i--)
#define pb push_back
#define ARR0(A) memset((A), 0, sizeof((A)))
#define ARR1m(A) memset((A), -1, sizeof((A)))
#define ARR0(A) memset((A), 0, sizeof((A)))
#define ARRINF(A) memset((A), 10000, sizeof((A)))

/*
Why did ceil did not work?
*/


typedef long long LL;
using namespace std;


void Q20171(){
    int t; scanf("%d\n",&t);

    FO(i,0,t)
    {   string s;int f;
        cin>>s>>f;

        int sol =0;
        FO(k,0,s.length()+1-f)
        {
            if(s[k]=='-')
            {   sol++;
                FO(j,0,f) 
                { 
                    if(s[k+j]=='-') 
                        s[k+j]='+';
                    else
                        s[k+j]='-';
                }

            }   
        }

        FO(k,0,s.length()) 
            if(s[k]=='-') sol=-1;

        if(sol==-1)
            cout<<"Case #"<<(i+1)<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<(i+1)<<": "<<sol<<endl;

    }
}

int dig[19];
void Q20172()
{   LL num;
    int t; scanf("%d\n",&t);

    FO(i,0,t)
    {   
        ARR0(dig);
        scanf("%lld\n",&num);

        int tdigits;
        FO(k,0,19)
            { dig[k]=num%10;
              num=num/10;
              if(num==0){tdigits=k+1;break;}
            }

        FO(k,0,tdigits)
        {
            FO(j,k+1,tdigits)
            {
                if(dig[k]<dig[j])
                { 
                    //cout<< dig[k]<<"::"<<dig[j]<<endl;
                    
                    dig[j] = dig[j]-1;   
                    RO(x,j-1,0)
                        dig[x]=9;

                    
                    
                }
            }
        }

        cout<<"Case #"<<(i+1)<<": ";
        //cout<<tdigits<<endl;
        RO(k,tdigits,0)
        if(dig[k]!=0)
        {
            cout<<dig[k];
        }
        cout<<endl;
    }
}

int main()
{   
    Q20171();
    //Q20172();
    //Q20153();
    return 0;
}
