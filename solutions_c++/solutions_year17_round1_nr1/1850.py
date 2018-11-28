#include<iostream>
#include<cmath>
#include<cstring>
#include<fstream>
#include<queue>
using namespace std;


int main()
{
    fstream fil;
	fil.open("C:\\Users\\vaibhav\\Desktop\\G_JAMA01.txt");
    int T,case_count=1;
    cin>>T;
    
    while(T)
    {
       
        int R,C;
        cin>>R>>C;
        char cake[R][C];
        for(int i=0;i<R;i++)
        {
            cin>>cake[i];
            
        }
        
        char curr='?';
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                if(cake[i][j]=='?')
                {
                    cake[i][j]=curr;
                }
                else
                {
                    curr=cake[i][j];
                    int k=j;
                    if(k>0 && cake[i][k-1]=='?')
                    {
                        k--;
                        while(k>=0 && cake[i][k]=='?')
                        {
                            cake[i][k]=curr;
                            k--;
                        }
                    }
                }
            }
            curr='?';
        }
        
        curr='?';
        
        for(int j=0;j<C;j++)
        {
            for(int i=0;i<R;i++)
            {
                if(cake[i][j]=='?')
                {
                    cake[i][j]=curr;
                }
                else
                {
                    curr=cake[i][j];
                    int k=i;
                    if(k>0 && cake[k-1][j]=='?')
                    {
                        k--;
                        while(k>=0 && cake[k][j]=='?')
                        {
                            cake[k][j]=curr;
                            k--;
                        }
                    }
                }
            }
            curr='?';
        }
        
        
        cout<<"Case #"<<case_count<<": \n";
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            cout<<cake[i][j];
            
            cout<<endl;
        }
        fil<<"Case #"<<case_count<<": \n";
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            fil<<cake[i][j];
            
            fil<<"\n";
        }
        case_count++;
        T--;
    }
    fil.close();
}
