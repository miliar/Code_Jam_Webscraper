#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;

//int check(int n,int s){
//	if(s==1) return n;
//	if(s==2)
//	{
//		if(n/10 > n%10)
//		{
//			return 10*(n/10) -1;
//			
//		}
//		else
//		return n;
//	}
//	if(s==3)
//	{
//		int a = n/100;
//		int b = n%100;
//		int c =(b/10);
//		if(a>c)
//		return n-b-1;
//		else
//		return a*10 + check(b,s-1);
//	}
//}
int check(int n,int s,int prev)
{
	
	if(n<=9)
	{
		//cout<<n<<"aa  "<<endl;
		return n;
	}
	else
	{
		int a = n/(pow(10,s-1));
		int b = n - a*pow(10,s-1);
		int c =(b/(pow(10,s-2)));
		if(prev == a && b < a )
		{
			return -1;
		}
		if(a>c)
		{
			return a * pow(10,s-1) -1;
			
		}
		else 
		{
		//	cout<<n<<"  ";
			return  a*pow(10,s-1) + check(b,s-1,a);
		}
		
		
	}
}

int main()
{
	ifstream myfile;
	myfile.open("input.in");
	ofstream urFile;
    urFile.open("ans.out");
    int t;
	myfile>>t;
	
	
	int i=1;
	while(t--)
	{
		int n;
		myfile>>n;
		int size = n > 9 ? (int) log10 ((double) n) + 1 : 1;
		n =check(n,size,0);
		urFile<<"Case #"<<i++<<": "<<n<<endl;
	}
	return 0;
}
