#include <iostream>
#include <cmath>
#include <cstdint>
#include <vector>
#include <utility>
#include <string>

typedef uintmax_t  UINT;
typedef intmax_t INT;

using namespace std;

void tidy(vector<UINT>& N)
{
    
    for(INT i=N.size()-1;i>=1;i--)
    {
        if(N[i]>=N[i-1])
        {
            
        }
        else
        {
            N[i-1]--;
            for(INT j=i;j<N.size();j++)
            {
                N[j]=9;
            }
        }
    }
    return;
}

int main(int argc,char ** argv)
{
    UINT T;
    UINT cases=0;
    cin>>T;
    string S;
    vector<UINT> N;
    S.reserve(19);
    N.reserve(19);
    while(T)
    {
        S.clear();
        N.clear();
        
        cases++;
        cout<<"Case #"<<cases<<": ";
        
        cin>>S;
        
        for(char c : S)
        {
            N.push_back(c-'0');
        }
        tidy(N);
        bool front=true;
        for(UINT i : N)
        {
            if(front && i==0)
            {
                front=false;
            }
            else
            {
                cout<<i;
            }
            
        }
        cout<<endl;
        T--;
    }
    return 0;
}