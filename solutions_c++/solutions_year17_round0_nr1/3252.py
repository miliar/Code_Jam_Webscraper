#include<iostream>
#include<string.h>

using namespace std;

char *arr;
int T;
int K;
int L;
int count;

//�Ѱܹ��� idx��° ���ɟ���� K���� �����´�.
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

//�տ������� '-'�� ������ �ε����� ã�Ƽ� �� ���ɟ���� K���� �������ش�.
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