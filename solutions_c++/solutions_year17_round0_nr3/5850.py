#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;


int main() {

    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin >> t;
    for(int test=0;test<t;test++)
    {
        int n,k;
        cin >> n >> k;
        int stall[n]={0};
        int pos(-1),lm(-1),rm(-1);
        for(int person=0;person<k;person++)
        {
            pos=-1,lm=-1,rm=-1;
            for(int i=0;i<n;i++)
            {
                int l(0),r(0);
                if(!stall[i])
                {
                    for(int j=i-1;j>=0;j--)
                    {
                        if(!stall[j]) l++;
                        else break;
                    }
                    for(int j=i+1;j<n;j++)
                    {
                        if(!stall[j]) r++;
                        else break;
                    }
                    int m=min(l,r),mm=max(l,r);
                    if(m>min(lm,rm)) pos=i,lm=l,rm=r;
                    else if(m==min(lm,rm))
                    {
                        if(mm>max(lm,rm)) pos=i,lm=l,rm=r;
                    }
                }
            }
            stall[pos]=1;
        }
        cout <<"Case #"<<test+1<<": "<< max(lm,rm) << " "<<min(lm,rm)<< endl;

    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
