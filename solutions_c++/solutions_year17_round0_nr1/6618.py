#include <fstream>
using namespace std;

int main() {
    fstream fin,fout;
    fin.open("input.in",ios::in);
    fout.open("output.out",ios::out);
	int t;
	fin>>t;
	for(int i=1;i<=t;i++)
	{
	    int n,k;
	    string s;
	    fin>>s;
	    n=s.size();
	    bool arr[n];
	    for(int j=0;j<n;j++)
	    {
	        if(s[j]=='-')
	            arr[j]=true;
	        else
	            arr[j]=false;
	    }
	    fin>>k;
	    bool flip=true;
	    int count=0;
	    for(int j=0;j<n-k+1;j++)
	    {
	        if(arr[j])
	        {
                for(int l=0;l<k;l++)
                    arr[j+l]^=1;
                count++;
	        }
	    }
	    for(int j=0;j<n;j++){
	        if(arr[j])
	        {
	            count=-1;
	            break;
	        }
	    }
	    fout<<"Case #"<<i<<": ";
	    if(count==-1)
	    fout<<"IMPOSSIBLE";
	    else
	    fout<<count;
	    fout<<endl;

	}
	return 0;
}
