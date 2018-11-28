#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
using namespace std;

long long power(int base,long long power);
bool checker(char *source);

int main()
{
 char N[100][1000];
 int loop_t,T;
 cin>>T;

 for(loop_t=1;loop_t<=T;loop_t++)
 {
     cin>>N[loop_t-1];
 }

 for(loop_t=0;loop_t<T;loop_t++)
 {
    if(checker(N[loop_t]))
    {
       cout<<"case #"<<loop_t+1<<": "<<N[loop_t]<<endl;
    }

 }

 return 0;
}

long long power(int base, long long power)
{

    long long x,result=1;
    for(x=power;x>=1;x--)
        result*=base;
    return result;
}

bool checker(char *source)
{
     bool check=true;
     long long ans,loop_i,loop_j,multiplier;
     if(strlen(source)==1)
        return check;
     else
     {
            for(loop_i=0;loop_i<strlen(source)-1;loop_i++)
            {
                if(source[loop_i]<=source[loop_i+1])
                    continue;
                else
                {
                    ans = 0;
                    check=false;
                    for(loop_j=0;loop_j<=loop_i;loop_j++)
                    {
                        ans*=10;
                        ans+=source[loop_j]-48;
                    }

                    multiplier = strlen(source)-loop_i-1;
                    ans=ans*power(10,multiplier);
                    ans--;
                    break;
                }
            }
            if(check==false)
            {
                lltoa(ans,source,10);

                checker(source);

            }
            else
                return true;


        }
}
