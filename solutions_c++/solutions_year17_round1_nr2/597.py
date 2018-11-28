#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <stack>
#include <queue>
using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef queue<ii> qii;
typedef vector<int> vi;

int target[50];
int data[50][50];

int main() {
  int TC;
  scanf("%d", &TC);
  for(int t = 1; t <= TC; ++t) {
    for(int i = 0; i < 50; ++i) {
      for(int j = 0; j < 50; ++j) {
        data[i][j] = 0;
      }
      target[i] = 0;
    }

    int N, P;
    scanf("%d %d", &N, &P);

    for(int i = 0; i < N; ++i) {
      scanf("%d", target+i);
    }

    for(int i = 0; i < N; ++i) {
      for(int j = 0; j < P; ++j) {
        cin >> data[i][j];
      }
    }

    vector<qii> num;
    num.assign(N, qii());
    for(int i = 0; i < N; ++i) {
      vii temp;
      for(int j = 0; j < P; ++j) {
        int low = (data[i][j]*10) / (target[i]*11);
        if((data[i][j]*10) % (target[i]*11) != 0) {
          low++;
        }
        int high = (data[i][j]*10) / (target[i]*9);
        if(low <= high) {
          temp.push_back(ii(low, high));
        }
      }
      sort(temp.begin(), temp.end());
      for(int x = 0; x < temp.size(); ++x) {
        num[i].push(temp[x]);
      }
    }
    
    int ans = 0;
    bool test = true;
    for(int i = 0; i < N; ++i) {
      if(num[i].empty()) {
        test = false;
      }
    }

    if(test) {
      while(true) {
        int minimax = 10000000;
        int minindex = 0;
        for(int i = 0; i < N; ++i) {
          if(num[i].front().second < minimax) {
            minimax = num[i].front().second;
            minindex = i;
          }
        }

        bool logic = true;
        for(int i = 0; i < N; ++i) {
          if(num[i].front().first > minimax) {
            logic = false;
            break;
          }
        }

        if(logic) {
          for(int i = 0; i < N; ++i) {
            num[i].pop();
          } 
          ans++;
        } else {
          num[minindex].pop();
        }

        if(num[minindex].empty()) {
          break;
        }
      }
    }

    printf("Case #%d: %d\n", t, ans);
  }
}