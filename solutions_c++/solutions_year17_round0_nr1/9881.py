#include<iostream>
#include<fstream>
#include<string.h>
#include<windows.h>
#include<conio.h>
#include<stdlib.h>

using namespace std;

int main() {

 ifstream myReadFile;
 ofstream myWriteFile;
 myReadFile.open("input.txt");
 myWriteFile.open("output.txt");
 char output[100];
 char input[100];
 int cs = 1;
 if (myReadFile.is_open()) {
 while (!myReadFile.eof()) {

    myReadFile >> output;
    int k = 0, j = 0, flip = 0, flag = 0;
    if(strcmp(output, "100")!=0 && cs <=100)
    {
    	if(output[j]=='+' || output[j]=='-')
    	{
    		strncpy(input, output, 100);
		}
		else
		{
			k = atoi(output);
			flag = 1;
		}
		if(flag == 1)
		{
			while(input[j]!='\0')
            {
    	      if(input[j]=='-')
    	       {
    		     if(j+k>strlen(input))
    		     {
    			  flag = 2;
    			  break;
			     }
    		     for(int i = j; i < j+k; i++)
    		     {
    			    if(input[i]=='-')
    			    input[i] = '+';
    			    else
    			    input[i] = '-';
			     }
			        flip++;
			        j = 0;
		       }
		         else   
		         {
			       j++;
	             }
	       }
	          if(flag == 2)
	          {
		        cout<<"Case #"<<cs<<": IMPOSSIBLE\n";
		        myWriteFile<<"Case #"<<cs<<": IMPOSSIBLE\n";
	          }
	          else
           	  {
		        cout<<"Case #"<<cs<<": "<<flip<<endl;
		        myWriteFile<<"Case #"<<cs<<": "<<flip<<endl;
	          }
	          cs++;
		}
	}
	
 }
}
myReadFile.close();
myWriteFile.close();
return 0;
}
