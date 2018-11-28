
// just use a heap of pair with size of the index of the gap and the size of the gap to the left as the second parameter(highest gap at the top, for equal gaps lowest index to the left)
#include<iostream> 
//#include<queue>
using namespace std;

long int power(int x, long int y)
{
    long int temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return ((long int)x)*temp*temp;
}


int countDigits(long int n)
{
	int c=0;
	while(n>0)
	{
		++c;
		n=n/10;
	}
	return c;
}

long int findAndReturnTidy(long int n)
{
	long int y=0, curDig, prevDig=0;
	int totDigCnt=countDigits(n), digitsExamined=0;
	int repDigCnt=1;
	long int zeros=power(10, totDigCnt-1);
	
	while(n>0)
	{
		curDig=n/zeros;
		++digitsExamined;
		//cout<<"curDig="<<curDig;
		if(curDig>prevDig)
		{
			repDigCnt=1;
		}
		else if(curDig==prevDig)
		{
			++repDigCnt;
		}
		else
		{
			break;
		}
		
		y=y*10+curDig;
		n=n%zeros;
		zeros/=10;
		prevDig=curDig;
		//cout<<" y="<<y<<" n="<<n<<" zeros="<<zeros<<endl;
	}
	if(n>0 || digitsExamined!=totDigCnt)//this means we found some point where the number becomes untidy
	{
		if(prevDig!=1)
		{
			zeros*=power(10, repDigCnt);
			long int temp = prevDig*zeros-1;
			y/=power(10, repDigCnt);
			y=y*zeros*10+temp;
		}
		else
		{
			y=0;
			for(int i=1; i<totDigCnt; ++i)
			{
				y=y*10+9;
			}
		}
	}
	return y;
}

int main()  
{
	long int n, y;
	int t;
	cin>>t;
	for(int i=1; i<=t; ++i)	
	{
		cin >> n;
		y=findAndReturnTidy(n);
		//cout << "Case #" << i << ": " << n << endl;
		cout << "Case #" << i << ": " << y << endl;
	}
	return 0;
}

