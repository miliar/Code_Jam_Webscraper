#include <iostream>
#include <fstream>
using namespace std;

bool isSorted(int n){

	int temp=n;
	int n1,n2;

	if(n<10)
		return true;

	
	n1=temp%10;
	temp=temp/10;
	while(temp>0){
		n2=temp%10;
		temp=temp/10;
		if(n2>n1)
		{
			return false;
		}
		n1=n2;
	}
	return true;

}

int main(){
	int tNumbers;
	int * numArr;

	ifstream fin("B-small-attempt0.in");
	if(fin.is_open())
	{
		fin>>tNumbers;
		numArr=new int[tNumbers]();
		int index = 0;
		int temp;
		while (!fin.eof())
		{
			fin>>temp;
			for (int i = temp; i >=1; i--)
			{
				if(isSorted(i))
				{
					numArr[index]=i;
					index++;
					break;
				}
			}
		}
	}
	else{
		cout<<"File could not open"<<endl;
	}

	fin.close();


	ofstream fout("Output.txt");
	if(fout.is_open()){
		for (int i = 0; i < tNumbers; i++)
		{
			fout<<"Case #"<<i+1<<": "<<numArr[i]<<endl;
		}
	}


	return 0;
}