#include<iostream>
using namespace std;
int main()
{
    int tt;
    cin>>tt;
    for(int ttt=1;ttt<=tt;ttt++)
    {
        cout<<"Case #"<<ttt<<":\n";
        int R,C;
        cin>>R>>C;
        char mat[R][C];
        
        for(int i=0;i<R;i++)
        {
            char runnineChar = '?';
            for(int j=0;j<C;j++)
            {
                cin>>mat[i][j];
                if(mat[i][j] != '?')
                {
                    for(int k=0;k<=j;k++)
                        if(mat[i][k] == '?')
                            mat[i][k] = mat[i][j];
                    
                    runnineChar = mat[i][j];
                }
                else if(mat[i][j] == '?' && runnineChar!='?')
                    mat[i][j] = runnineChar;
                    
            }
        }
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                if(mat[i][j] == '?')
                {
                    bool found=false;
                    for(int k=i-1;k>=0;k--)
                    {
                        if(mat[k][j] != '?')
                        {
                            found = true;
                            mat[i][j] = mat[k][j];
                            break;
                        }
                    }
                    if(found == false)
                    {
                        for(int k=i+1;k<R;k++)
                        {
                            if(mat[k][j] != '?')
                            {
                                found = true;
                                mat[i][j] = mat[k][j];
                                break;
                            }
                        }
                    
                    }
                    if(found == false)
                        cout<<"Error\n"<<endl;
                }
            }
        }
            
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
                cout<<mat[i][j];
            
                cout<<endl;
        }
    
        
    
    }
}
