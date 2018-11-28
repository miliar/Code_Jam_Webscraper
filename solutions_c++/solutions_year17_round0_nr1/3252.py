#include<iostream>
#include<string.h>

using namespace std;

char *arr;
int T;
int K;
int L;
int count;

//넘겨받은 idx번째 팬케잌부터 K개를 뒤집는다.
void Flip(int idx)
{
	for(int i=0;i<K;i++)
	{
		if(arr[idx+i]=='+')
			arr[idx+i]='-';
		else if(arr[idx+i]=='-')
			arr[idx+i]='+';
	}		
}

//앞에서부터 '-'가 나오는 인덱스를 찾아서 그 팬케잌부터 K개를 뒤집어준다.
void LoopFlip()
{
	count = 0;
	for(int i=0;i<L-K+1;i++)
		if(arr[i]=='-')
		{
			Flip(i);
			count++;
		}	
	for(int i=0;i<L;i++)
		if(arr[i]=='-')
		{
			cout<<"IMPOSSIBLE"<<endl;
			return;
		}

	cout<<count<<endl;	
}

int main()
{
	cin>>T;
	for(int i=0;i<T;i++)
	{	
		arr = new char[1000];
		cin>>arr;
		cin>>K;

		L = strlen(arr);
		cout<<"Case #"<<i+1<<": ";
		LoopFlip();	
	}


	return 0;
}