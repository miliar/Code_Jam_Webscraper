#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream fileinput;
    ofstream myfile;
    fileinput.open("B-small-attempt0.in");
    myfile.open("output.txt");
    int t;int i=1;
    fileinput>>t;
    while(t--)
    {
        int num;
        fileinput>>num;
        while(1)
        {
            int flag=0;
            int temp=num;
            while(temp!=0)
            {
                int a=temp%10;
                temp/=10;
                int b=temp%10;
                if(a>=b)
                    continue;
                else
                {
                    flag=1;
                    break;
                }
            }
            if(flag!=0)
            num--;
            else
            {
                myfile<<"case #"<<i++<<": "<<num<<endl;
                break;
            }

        }
    }
}
