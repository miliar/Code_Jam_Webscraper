#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
    long long int n;
    cin >> n;
    int arr[19];
    for(long long int i= n; i > 0; i--)
    {
      bool flag = true;
      int index = 0;
      int temp = i;
      while(temp)
      {
        arr[index++] = temp%10;
        temp = temp/10;
      }
      for(int j = 0; j < index-1; j++)
      {
        if(arr[j] < arr[j+1])
        {
          flag = false;
          break;
        }
      }
      if(flag)
      {
        cout << "Case #" << t << ": " <<i;
        break;
      }
    }
    cout << "\n";
  }
}
