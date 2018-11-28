#include <iostream>
#include <string>
#include <fstream>
using namespace std;
string arr;
int pan;
void turn(int a)
{
    for(int i=0;i<pan;i++)
    {
        if(arr[a+i]=='+')arr[a+i]='-';
        else arr[a+i]='+';
    }
}
int main()
{
    ifstream cinn("input.txt");
    ofstream coutt("output.txt");
    int T;
    cinn>>T;
    for(int tc=0;tc<T;tc++)
    {
        int answer=0;
        cinn>>arr>>pan;
        for(int i=0;i<arr.size()-pan+1;i++)
        {
            if(arr[i]=='-')
            {
                turn(i);
               // cout<<arr<<endl;
                answer++;
            }
        }
        int chk=0;
        for(int i=0;i<arr.size();i++)
        {
            if(arr[i]=='-')chk=1;
        }
        if(chk==0)
        coutt<<"Case #"<<tc+1<<": "<<answer<<endl;
        else coutt<<"Case #"<<tc+1<<": "<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
