#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
bool is_ascend(std::vector<int> input){
	bool check=1;
	int where=0;
	while(check && where<input.size()-1){
		int num1=input[where];
		int num2=input[where+1];
		if (num1<num2){
			check=0;
		}		
		//cout<<num1<<num2<<':'<<check<<endl;
		//check=(num1>=num2);
		where++;
	}		
	//cout<<"------------------------------------"<<endl;
	return check;
}

vector<int> checkdigit(long long number){
	std::vector<int> temp;
	long long q=1;
	long long num=number;
	long long rem;
	while(q!=0){
		rem=num%10;
		q=num/10;
		num=q;
		temp.insert(temp.begin(),rem);
	}
	return temp;
}

bool equal_vectors(std::vector<int> v1,std::vector<int> v2){
	bool check=1;
	for (int i = 0; i < v1.size(); ++i)
	{
		if(v1[i]!=v2[i]){
			check=0;
			break;
		}
	}
	return check;
}

int main(int argc, char const *argv[])
{
	freopen("B-small-attempt1.in", "r", stdin);
    freopen("B1.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	 for (int i = 0;i<tt;i++)
     {

	long long input;
	cin>>input;
	cout<<"Case #"<<i+1<<": ";
	for (long long i = input; i > 0; i--)

	{
		vector<int>numbers,vec_sort;
		numbers=checkdigit(i);
		//reverse(numbers.begin(),numbers.end());
		vec_sort=numbers;
		sort(vec_sort.begin(),vec_sort.end());
		if(vec_sort==numbers){
			cout<<i;
			break;
		}
	}
	cout<<endl;
}
	return 0;
}

