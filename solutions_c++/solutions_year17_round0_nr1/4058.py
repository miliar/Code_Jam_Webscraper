#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>

using namespace std;

void flip(string &s,int start,int k)
{
    for(int i=0;i<k;i++) s[start+i] = s[start+i] == '+' ? '-' : '+';
    return;
}

int check(string &s,int length,int k)
{
    for(int i=0;i<k-1;i++)
    {
        if(s[length-i] == '-') return 0;
    }
    return 1;
}

int main() {
	ifstream in;
	in.open("inputLarge.txt");
	ofstream out;
	out.open("outputLarge.txt");
	int t;
	in>>t;
	int cases = 0;
	while(t--)
	{
	    cases++;
		string s;
		int k;
		in>>s>>k;
		int length = s.length();
		int cnt=0;
		for(int i=0;i<length-k+1;i++)
        {
            if(s[i] == '-')
            {
                cnt++;
                flip(s,i,k);
            }
        }
        out<<"Case #"<<cases<<": ";
        if(check(s,length-1,k)) out<<cnt<<endl;
        else out<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
