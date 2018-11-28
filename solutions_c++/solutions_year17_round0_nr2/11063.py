#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int num_digits(int number)
{
    int digits = 0;
    if (number < 0) digits = 1;
    while (number) {
        number /= 10;
        digits++;
    }
    return digits;
}

int cal_last_tidynum(int n)
{
        int arr_size = num_digits(n);
 	if(arr_size  == 1) return n;
        
	int *arr = new int[arr_size];

	//if(num_digits == 1) return n;

//	cout <<"Arr Size :"<< arr_size << std::endl;
	int num = n;
//	cout << " Array:";
	for(int i=(arr_size-1); num > 0; i--)
	{
	   arr[i] = num%10;
           num = num/10;
//	   cout << arr[i] << " ";
        }
       
        int ans = 0 ;
	int i = 0;
	for(i= 0; i < arr_size; i++)
        {
		if(i == (arr_size-1)) { 
			ans = (ans * 10) + arr[i];
			break;
		}

		if(arr[i] <= arr[i+1]) {
			ans = (ans*10) + arr[i];
		}
                else {
			int total_digits_iterated = i;
			int cur_pos = i;
			
			while(cur_pos > 0) {
				if((arr[cur_pos]-1) < arr[cur_pos-1]){
					cur_pos--;
					ans = (ans - ans%10)/10;
				}
				else
					break;
			}  		
		
			ans = (ans*10) + (arr[cur_pos] - 1);
			i = cur_pos;
			break;
		} 		 
	}
	for(int j = i+1; j < arr_size; j++)
		ans = (ans *10) + 9;
 
        free(arr);
	return ans;
}

int main() {
  int t, n, ans;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
    if(n<0) cout << "Invalid input";
    ans = cal_last_tidynum(n);
    cout << "Case #" << i << ": " << ans  << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}
