#include<iostream>
#include<fstream>
#include<vector>
#include<bits/stdc++.h>

using namespace std;

long long int getMaximum(long long int c,long long int d)
{
    return (c>d)?c:d;
}

long long int getMinimum(long long int x,long long int y)
{
    return (x<y)?x:y;
}

void getForEven(long long int l,long long int u,long long int &mini,long long int &maxi,long long int &k)
{
    long long int middle;
    middle=(l+u)/2;
    k=k/2;
    if(k == 1)
	{
        mini = getMinimum(middle-l,u-middle);
        maxi = getMaximum(middle-l,u-middle);
        return;
    }
    else
	{
        if(k%2 == 0)
		{
            getForEven(middle+1,u,mini,maxi,k);
        }
        else
		{
            getForEven(l,middle-1,mini,maxi,k);
        }
    }
}

void getForOdd(long long int l,long long int u,long long int &mini,long long int &maxi,long long int &k)
{
    long long int middle;
    middle=(l+u)/2;
    k=k/2;
    if(k == 1)
	{
        mini = getMinimum(middle-l,u-middle);
        maxi = getMaximum(middle-l,u-middle);
        return;
    }
    else
	{
        if(k%2 == 0)
		{
            getForOdd(middle+1,u,mini,maxi,k);
        }
        else
		{
            getForOdd(l,middle-1,mini,maxi,k);
        }
    }
}

void getNo(long long int n,long long int k,ofstream &op)
{
    long long int l=1,u=n,mini=0,maxi=0;
    if(n%2 == 1)
	{
        if(k == 1)
		{
            mini=n/2;
            maxi=n/2;
        }
        else if(k%2 == 0)
		{
            getForOdd(1,n/2,mini,maxi,k);
        }
        else
		{
            getForOdd(((n+1)/2)+1,n,mini,maxi,k);
        }
    }
    else
	{
        if(k == 1){
            mini = n/2-1;
            maxi = n/2;
        }
        else if(k%2 == 0)
		{
            getForEven(n/2+1,n,mini,maxi,k);
        }
        else
		{
            getForEven(1,n/2-1,mini,maxi,k);
        }
    }
    op<<maxi<<" "<<mini<<endl;
}

int main()
{
    int test_case,x;
    long long int y,k;
    string str;
    ifstream input;
    ofstream output;
    input.open("big.in");
    output.open("abcd.txt");
    input>>test_case;
    for(x=1;x<=test_case;x++)
	{
        input>>y>>k;
        output<<"Case #"<<x<<": ";
        getNo(y,k,output);
    }
    return 0;
}
