#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstdio>
using namespace std;


int main() {
  int t;
  cin >> t;
  for(int nr = 1; nr <= t; nr ++) {
    int c, j, a, b;
    cin >> c >> j;
    pair <pair <int, int>, int> p[c+j];
    for(int i = 0; i < c; i ++) {
      cin >> p[i].first.first >> p[i].first.second;
      p[i].second = 0;
    }
    for(int i = c; i < c + j; i ++) {
      cin >> p[i].first.first >> p[i].first.second;
      p[i].second = 1;
    }
    
    vector <int> bardzo_dobre, srednie,  bardzo_zle;
    
    sort(p, p + c + j);
    
    int l0 = 0, z = 0;
    int cz = 2 * 12 * 60;
    
   if(p[0].second == 1) {
        if(p[c+j-1].second == 1) {
          if(p[0].first.first - p[c + j-1].first.second + cz) {
            bardzo_dobre.push_back(p[0].first.first - p[c + j-1].first.second + cz);
            z += 2;
          }
        } else {
          if(p[0].first.first - p[c+j-1].first.second + cz) {
            srednie.push_back(p[0].first.first - p[c +j -1].first.second + cz);
          }
          z ++;
        }
        //cout<< ".." << l0 << endl;
        l0 += p[0].first.first - p[c + j -1].first.second + cz;
      } else {
        if(p[c + j-1].second == 1) {
          if(p[0].first.first - p[c + j-1].first.second + cz) {
            srednie.push_back(p[0].first.first - p[c + j-1].first.second + cz);
          }
          z ++;
        } else {
          bardzo_zle.push_back(p[0].first.first - p[c+j-1].first.second +cz);
        }
        //cout<< "--" << l0 << " " << p[0].first.second << " " << p[c + j-1].first.second << " " << cz << endl;
        l0 += p[0].first.second - p[c + j-1].first.second + cz;
        //cout<< "-+-" << l0 << endl;
      } 
    //cout<< "Z" << z << endl;
    
    for(int i = 1; i < c + j; i ++)  {
      //cout<< p[i].second;
      if(p[i].second == 1) {
        if(p[i-1].second == 1) {
          if(p[i].first.first - p[i-1].first.second) {
            bardzo_dobre.push_back(p[i].first.first - p[i-1].first.second);
            z += 2;
          }
        } else {
          if(p[i].first.first - p[i-1].first.second) {
            srednie.push_back(p[i].first.first - p[i-1].first.second);
          }
          z ++;
        }
        //cout<< ".." << l0 << endl;
        l0 += p[i].first.first - p[i-1].first.second;
      } else {
        if(p[i-1].second == 1) {
          if(p[i].first.first - p[i-1].first.second) {
            srednie.push_back(p[i].first.first - p[i-1].first.second);
          }
          z ++;
        } else {
          bardzo_zle.push_back(p[i].first.first - p[i-1].first.second);
        }
        //cout<< "--" << l0 << endl;
        l0 += p[i].first.second - p[i-1].first.second;
      } 
    //cout<< l0 << endl;
    }
    
   cz = cz / 2;
  //cout<< l0 << " " << z << endl;
    sort(bardzo_dobre.rbegin(), bardzo_dobre.rend());
    sort(bardzo_zle.begin(), bardzo_zle.end());
   
    
    while(l0 > cz) {
      if(bardzo_dobre.size()) {
        l0 -= bardzo_dobre.back();
        //cout << "D" << bardzo_dobre.back();
        bardzo_dobre.pop_back();
        if(l0 >= cz) {
          z -= 2;
        }
      } else if(srednie.size()) {
        l0 -= srednie.back();
        srednie.pop_back();
      } else {
      //cout << "Z" << bardzo_zle.back();
        l0 -= bardzo_zle.back();
        bardzo_zle.pop_back();
        z += 2;
      }
    }
    
    cout<< "Case #" << nr <<": ";
    cout<< z;
    cout<< endl;
  }
  
}
