#include<iostream.h>
#include<string.h>
#include<sstream>
#include<conio.h>
#include<fstream.h>

using namespace std;

string IntTStr(int a)
{
    ostringstream temp;
    temp<<a;
    return temp.str();
}

int CheckTidy(string Arr)
{
    char prev=Arr.at(0);
    for(int i=1;i<Arr.length();i++)
    {
             if(Arr.at(i)<prev)
                return 0;
             prev=Arr.at(i);
            }
    return 1;
    }

int T;

int main()
{
    ifstream fi;
    fi.open("S_input.in",ios::in);
    ofstream fo;
    fo.open("S_output.txt",ios::out);
    //files opened...
    int Num[100];
    string NumS[100];
    fi>>T;
    //input taken
    //Conversion to String
    for(int i=0;i<T;i++)
    {
            fi>>Num[i];
            NumS[i]=IntTStr(Num[i]);
            }
    int Res;
    for(int i=0;i<T;i++)
    {
            repeat:
            Res=CheckTidy(NumS[i]);
            if(Res==0)
            {
                Num[i]-=1;
                NumS[i]=IntTStr(Num[i]);
                goto repeat;
                }
            }
            
    //Outputting now
    for(int i=0;i<T;i++)
    {
            fo<<"Case #"<<i+1<<": "<<Num[i]<<endl;
    }
            
    //file closing now...
    fi.close();
    fo.close();
    return 0;
    }
