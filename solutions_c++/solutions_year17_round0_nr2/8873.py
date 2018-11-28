#include<stdio.h>
#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;
int array[20];
void convert(char s[20])
{
		for (int i = 0; i < strlen(s) - 1; i++) 
                {
			if (array[i] > array[i + 1]) 
                        {
				array[i] -= 1;
				for (int j = i + 1; j < strlen(s); j++)    
					array[j] = 9;
				
				i = -1;
			}
}
}
int main() {
   
   ifstream fin("B-large.in");
 ofstream fout("B_large_output.txt"); 

	int t;
        fin>>t;
	for (int j = 1; j <= t; j++) 
        {
		char s[20];
                fin>>s;
		for (int i = 0; i < strlen(s); i++) 
                    array[i] = s[i]-'0';
	
		
		convert(s);
		int i= 0;
		while (array[i] == 0) 
                    i++;
		fout<<"Case #"<<j<<": ";
		for (int k=i; k < strlen(s); k++) 
                    fout<<array[k];
	fout<<endl;
	}
} 
