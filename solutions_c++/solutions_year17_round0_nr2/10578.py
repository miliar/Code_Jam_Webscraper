#include <iostream>
#include <fstream>
using namespace std;
int main(){
	ifstream in("sub-6.txt");
	ofstream out("store.txt");
	int testCase, casse=1, j, i, temp1, count; 
	in >> testCase;
	int array[testCase], temp2[4];
	for (int m=0; m<testCase; m++)
		in >> array[m];
	for (i=0; i<testCase; i++){
		while (true){
			count=0; j=0;  temp1=array[i];
			while (temp1!=0){
				temp2[j]=temp1%10;	// temp2 stores the digits
				temp1=temp1/10;	// temp1 stores the divised number
				j++;
			}
		for (int k=j-1; k>=0; k--){
			for (int l=k-1; l>=0; l--){
				if (temp2[k]>temp2[l]){
					count++;
					break;
				}
			}
			if (count!=0)
				break;	
		}
		if (count==0){
			out << "Case #" << casse << ": " <<array[i] << '\n';
			casse++;
			break;
		}
		else
			array[i]--;			
		}
	}
	out.close();
	return 0;
}