#include<iostream>
#include<cstdio>
#include<iomanip>


using namespace std;

#define size 20

int flipMyCake(int length_of_cake_array, int size_of_pan);
bool flip(int start_position_of_flip,int number_of_pancakes,int size_of_flipper);

char a[size];
int j,len;

int main(){
	char ch;	
	int T;
	int K;

	cin>>T;

	for(int i =0; i<T; i++){
		j = 0;
		
		//flush array
		for(int k =0 ; k<size;k++)
			a[k] = (char)NULL;

		ch = getchar();
		//input pancakes
		while(ch=getchar())
		{
			if((ch!=' '))
				a[j]=ch;
			else
				break;
			j++;

		}

		//length of row
		len = j;

		//input flipper size
		cin>>K;
		
//		printf("Initial : %s || ",a);

		//find minimum flips
		int val = flipMyCake(len,K);
		
		//cout<<"Case #"<<i+1<<": "<<val<<endl;
	//	for(int i1 =0; i1<len;){
	//		cout<<"\nChar : "<<i1<<a[i1];
	//		if(a[i1++]=='-')
	//			val = -1;
	//	}

		//print output
		if(val==-1)
			cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<i+1<<": "<<val<<endl;


	//	printf("Final :  %s || ",a);
	//	cout<<"Case #"<<i+1<<": "<<" K= "<<K<<" len= "<<len<<"  //"<<val<<endl;
	//	cout<<"\n\n";
		
	}
	return 0;
}

int flipMyCake(int l, int k){

	//boundary conditions
	if(k>l)
		return -1;
	
	bool d;
	int count = 0;


	/*	
	int flag1 = 0;
	int flag2 = 0;

	for(int i =0;i<k-1;i++)
	{
		if(a[i]!=a[i+1])
			{ flag1 = 1; break; }
	}
	for(int i =len-2;i>len-1-k;i--)
	{
		if(a[i]!=a[i+1])
			{ flag2 = 1; break; }
	}
	if((flag1 == 1) && (flag2 == 1))
		return -1;
	else{
	*/


	//Finding minimum number of flips.
		for(int i=0;i<l;i++){
			if(a[i]=='-'){ 
				d = flip(i,l,k);
				count++;
				if(d == false)
					return -1;
			}
		}
		return count;
}

bool flip(int i,int l,int k){
	
	//flipper crosses the wall
	if((i+k-1)>=l){	
//		cout<<"entered"<<i<<k<<l;
		return false;
	}

	for(int p=i;p<i+k;p++){
		if(a[p] == '-')
			a[p] = '+';
		else 
			a[p] = '-';
	}
	 //printf(" %s || ",a);
	return true;
}