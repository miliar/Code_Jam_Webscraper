#include <iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;

int main() {
	// your code goes here
	//ifstream fin;
	//fin.open("name.txt");
	
	int cases;
	cin>>cases;
	//cout<<cases<<endl;
	for(int cc=0;cc<cases;cc++)
	{
	    int r;
	    int c;
	    cin>>r;
	    cin>>c;
	    
	    char **arr = new char*[r];
	    for(int i=0;i<r;i++)
	        arr[i] = new char[c];
	   
	   vector<char> mem;
	        
	    for(int i=0;i<r;i++)
	    {
	        string str;
	        cin>>str;
	        for(int a =0;a<str.length();a++)
	        {
	            arr[i][a] = str[a];
	            if(str[a]!='?')
	                mem.push_back(str[a]);
	        }
	        
	    }
	    
	    for(int i=0;i<r;i++)
	    {
	        for(int j=0;j<c;j++)
	        {
	            if(arr[i][j]=='?')
	            {
	                if(j+1<c && arr[i][j+1]!='?')
	                    arr[i][j] = arr[i][j+1];
	                else if(i+1<r && arr[i+1][j]!='?')
	                    arr[i][j] = arr[i+1][j];
	                else if(j-1>=0 &&  arr[i][j-1] !='?')
	                    arr[i][j] = arr[i][j-1];
	                else
	                    arr[i][j] = mem[0];
	                   
	            }
	        }
	    }
	    cout<<"Case #"<<cc+1<<":\n";
	    for(int i=0;i<r;i++)
	    {
	        for(int j=0;j<c;j++)
	        {
	            cout<<arr[i][j];
	        }
	        cout<<endl;
	    }
	   
	}
	return 0;
}

