#include<iostream>
using namespace std;

class BathroomStalls
{
	private:
	int t, n, k;
	int* stalls;
	
	public:
	
	BathroomStalls(int x)
	{
		t = x;
		cin>>n>>k;
		//stalls = new int[n];
		
		stalls = new int[n];
		
		for(int i=0; i<n; ++i)
			stalls[i] = 0;
		
		int a = 0, b = n-1, gap = n;
		//++stalls[(a+b)/2];
		
		int pos;
		
		for(int i=0; i<k; ++i)
		{
			
			/*for(int i=0; i<n; ++i)
				cout<<stalls[i];
			cout<<"\n";*/
			
			gap = 0; int c = 0;
			int start = 0; b = 0;
			for(int j=0; j<=n; ++j)
			{
				if(stalls[j] != 0 || j == n)
				{
					if(c>gap)
					{
						gap = c;
						c = 0;
						a = start;
						b = j-1;
						start = j+1;
					}
					else
					{
						c = 0;
						start = j+1;
					}
				}
				else
				{
					++c;
					
				}
			}
			//display(gap);
			pos = (a+b)/2;
			//cout<<"pos a b"<<pos<<" "<<a<<" "<<b<<"\n";
			++stalls[pos];
		}
		
		//cout<<"pos "<<pos<<"\n";
			
		int flag = 1;
		
		int min = 0, max = 0;
		
		while(flag>0)
		{
			int dmmy = pos-1;
			//cout<<dmmy<<"\n";
			int c = 0;
			while(stalls[dmmy] == 0){
				if(dmmy<0)
					break;
				++c;
				--dmmy;
				//cout<<"c dmmy "<<c<<" "<<dmmy<<"\n";
			}
			//cout<<pos<<"\n";
			min = c;
			c = 0;
			dmmy = pos+1;
			//cout<<dmmy<<"\n";
			while(stalls[dmmy] == 0) {
				if(dmmy>=n)
					break;
				++c;
				++dmmy;
				//cout<<"c dmmy "<<c<<" "<<dmmy<<"\n";
			}
			
			
			
			max = c;
			
		
			//display(min, max);
			flag = 0;
		}
		
		
		if(n == k)
		{
			min = 0;
			max = 0;
		}
			
		display(min, max);
			
			//if(gap%2 == 0)
			
		
		
	
		
		//display(gap);
	
	}
	
	/*void display(int max, int min)
	{
		for(int i=0; i<n; ++i)
			cout<<stalls[i]<<"\t";
		cout<<"\n";
	}*/
	
	void display(int min, int max)
	{
		/*for(int i=0; i<n; ++i)
			cout<<stalls[i]<<"\t";
		cout<<"\n";*/
		
		cout<<"Case #"<<t<<": "<<max<<" "<<min<<"\n";
	}
	
	/*void placeFirst()
	{
		++stalls[(n-1)/2];
		return (n-1)/2;
	}
	
	void place(int a, int b)
	{
		++stalls((a+b+1)/2);
	}
	
	void display()
	{
		for(int i=0; i<n; ++i)
			cout<<arr[i];
		cout<<"\n";
	}*/
};

int main()
{
	int t;
	cin>>t;
	
	BathroomStalls** obj = new BathroomStalls*[t];
	for(int i=0; i<t; ++i)
		obj[i] = new BathroomStalls(i+1);
}