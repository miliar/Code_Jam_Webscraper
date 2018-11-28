#include<iostream>
#include<cmath>
#include<cstring>
#include<fstream>
using namespace std;

char Switch(char a)
{
    if(a=='-')
    return '+';
    else
    return '-';
}
int main()
{
    fstream fil;
	fil.open("C:\\Users\\vaibhav\\Desktop\\G_JAM01.txt");
    int T,case_count=1;
    cin>>T;
    
    while(T)
    {
        char S[1000];
        int K;
        cin>>S>>K;
        int flip_count = 0;
        
        for(int i=0;i<=strlen(S)-K;i++)
        {
            if(S[i]=='-')
            {
                for(int k=i;k<i+K;k++)
                S[k]=Switch(S[k]);
                flip_count++;
            }
            else continue;
        }
        
        bool possible=true;
        for(int i=0;i<strlen(S);i++)
        {
          if(S[i]=='-')
          possible=false;  
        }
        if(possible)
        {
            cout<<"Case #"<<case_count<<": "<<flip_count<<endl;
            fil<<"Case #"<<case_count<<": "<<flip_count<<"\n";
        }
        else
        {
            cout<<"Case #"<<case_count<<": IMPOSSIBLE"<<endl;
            fil<<"Case #"<<case_count<<": IMPOSSIBLE"<<"\n";
        }
        case_count++;
        T--;
    }
    fil.close();
}
