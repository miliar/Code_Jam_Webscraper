#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
char pancake[1001];
int size;
int invert(int i)
{
    for (int j=0;j<size; j++)
    {
        if (pancake[i]=='-')
        {pancake[i] = '+';
            cout<<"yes"<<endl;}
        else
            pancake[i] ='-';
        i++;
    }
}
int main()
{
    int caseNo=1,t,temp,i,j,len,count=0,flag,symbol;
    ifstream input;
    ofstream output;
    output.open("output.txt");
    input.open("input.txt");
    input>>t;
    //cout<<t;
    while(caseNo<=t)
    {
        //input>>
        count =0;
        input>> pancake >> size;
        //cout << pancake <<size <<endl;
        i=0;
        len=strlen(pancake);
        //cout << len <<endl;
        i=0;
        while(i<len-size)
        {
            if (pancake[i] == '-')
            {
                count++;
                invert(i);
                cout<< pancake<<endl;
            }
            i++;
        }
        symbol = pancake[i];
        if (symbol =='-')
            count++;
        i++;
        flag = 0;
        while (i<len)
        {
            if (pancake[i] == symbol)
                flag = 0;
            else
            {
                flag = 1;
                break;
            }
            i++;
        }
        if (flag == 1)
            output<<"Case #"<<caseNo<<": "<<"IMPOSSIBLE"<<endl;
        else
            output<<"Case #"<<caseNo<<": "<<count<<endl;

        //f<<caseNo;
        caseNo++;
    }
    input.close();
}
