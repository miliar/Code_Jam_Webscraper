#include<iostream.h>
#include<conio.h>
#include<fstream.h>

using namespace std;

int Check(char []);
int T;

int main()
{
    ifstream fi;
    fi.open("S_input.in",ios::in);
    ofstream fo;
    fo.open("S_output.txt",ios::out);
    //files opened...
    char cook[100][1000];
    int limit[100],count[100];
    fi>>T;
    for(int i=0;i<T;i++)
    {
            fi>>cook[i];
            fi>>limit[i];
            }
    int FLAG=0,Res;
    //Taken Input
    for(int j=0;j<T;j++)
    {
            FLAG=0;
            count[j]=0;
            int k=0;
            for(;cook[j][k]!='\0';k++)
            {
                    if(cook[j][k]=='+')
                    {
                                       continue;
                                       }
                    else if(cook[j][k]=='-')
                    {
                     int m,temp;
                                       for(temp=k,m=0;m<limit[j];m++,temp++)
                                       {
                                                count[j]++;
                                                              
                                               if(cook[j][temp]=='+')
                                                  cook[j][temp]='-';
                                               else if(cook[j][temp]=='-')
                                                    cook[j][temp]='+';
                                               else if(cook[j][temp]=='\0')
                                                    FLAG=-1;      
                                        }
                      //if(cook[j][k]=='\0')
                      //{
                      //                      Res=Check(cook[j]);
                      //                   if(Res==0)
                      //                             count[j]=-1;
                      //                             break;
                     // } 
                      if(FLAG==-1)
                                  count[j]=-1;
                     }
             }
    }
    //Calculated the Value
    
    for(int i=0;i<T;i++)
    {
            if(count[i]!=-1)
                            fo<<"Case #"<<i+1<<": "<<count[i]/limit[i]<<endl;
            else
                fo<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
    }
    
    //file closing now...
    fi.close();
    fo.close();
    getch();
    return 0;
}
    
int Check(char arr[])
{
    for(int i=0;i<T;i++)
    {
     if(arr[i]=='-')
                    return 0;
    
    }
    return 1;
    }    
