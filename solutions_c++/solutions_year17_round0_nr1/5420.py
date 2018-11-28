#include<iostream>
#include<string.h>
#include<string>
#include<algorithm>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("/Users/abdulaleemkhan/Desktop/input/in4.txt");
    fout.open("/Users/abdulaleemkhan/Desktop/input/out4.txt");

    int cases;
    fin>>cases;
    for(int cc=0;cc<cases;cc++)
    {
        string str;
        fin>>str;
        int k;
        fin>>k;
        int l = str.length();
        int count =0;
        for(int i=0;i<l-k+1;i++)
        {
            if(str[i]=='+')
            {}
            else
            {
                for(int j=i;j<i+k;j++)
                {
                    if(str[j]=='-')
                        str[j]='+';
                    else
                        str[j]='-';
                    
                }
                count++;
            }
        }
        bool flag = true;
        for(int i=0;i<l;i++)
        {
            if(str[i]=='-')
            {
                fout<<"Case #"<<cc+1<<": "<<"IMPOSSIBLE\n";
                flag = false;
                break;
            }
            
        }
        if(flag)
            fout<<"Case #"<<cc+1<<": "<<count<<endl;
        
    }
    
    return 0;
}
