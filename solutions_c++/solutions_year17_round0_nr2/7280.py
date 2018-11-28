/** source code by coolreshab **/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,i,j,len,dragon=1;
    long long N;
    vector<int>digits;
    cin>>T;
    while(T-->0)
    {
        cin>>N;
        while(N)
        {
            digits.push_back(N%10);
            N/=10;
        }
        len=digits.size();
        for(i=1;i<len;++i)
        {
            if(digits[i]>digits[i-1])
            {
                digits[i]-=1;
                j=i-1;
                while(j>=0)
                    digits[j--]=9;
            }
        }
        i=len-1;
        if(digits[len-1]==0)
            i-=1;
        cout<<"Case #"<<dragon<<": ";
        for(;i>=0;--i)
            cout<<digits[i];
        cout<<endl;
        digits.clear();
        dragon+=1;
    }
    return 0;
}
