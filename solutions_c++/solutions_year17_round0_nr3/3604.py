#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

//std::map<int, std::map<int, Room> > m;

class Room{
public:
  int i;
  int ld;
  int rd;
  bool operator<(const Room& ri){
    if(std::min(ld, rd) != std::min(ri.ld, ri.rd))
      return std::min(ld, rd) > std::min(ri.ld, ri.rd);
    else if(std::max(ld, rd) != std::max(ri.ld, ri.rd))
      return std::max(ld, rd) > std::max(ri.ld, ri.rd);
    else
      return i > ri.i;
  }
};

inline int getld(const std::vector<bool>& arr, int p){
  int nowd = 0;
  for(int i = p-1; i >= 0; i--){
    if(arr[i])
      return nowd;
    nowd++;
  }
}
inline int getrd(const std::vector<bool>& arr, int p){
int nowd = 0;
  for(int i = p+1; i < arr.size(); i++){
    if(arr[i])
      return nowd;
    nowd++;
  }
}

/*
min(LS, RS) is maximal
max(LS, RS) is maximal
the leftmost stall
*/

Room chooseMinRoom(const std::vector<bool>& arr){
  std::vector<Room> rooms;
  for(int i = 1; i < arr.size()-1; i++)//1~n
    if(!arr[i]){
      Room r;
      r.ld = getld(arr, i);
      r.rd = getrd(arr, i);
      r.i = i;
      rooms.push_back(r);
    }
  std::sort(rooms.begin(), rooms.end());
  return rooms[0];
}

Room getSideDistance(int n, int k){
  Room room;
  room.ld = 0; room.rd = 0;
  //if(k > n/2)
  //    return room;
  std::vector<bool> arr;
  arr.resize(n+2);
  std::fill(arr.begin(), arr.end(), false);
  arr[0] = true;
  arr[n+1] = true; 
  for(int i = 0; i < k; i++){
    room = chooseMinRoom(arr);
    arr[room.i] = true;
    //fprintf(stderr, "%d user, room %d, (%d, %d)\n", i, room.i, room.ld, room.rd);
  }
  return room;
}



Room getSideDistance2(int n, int k){
  int mid= n/2;
  int midpower = 0;
  while(mid > 0){
    mid/=2;
    midpower++;
  }
  mid = 1;
  for(int i = 0; i < midpower; i++)
    mid *= 2;
  //printf("(%d, %d), mid %d\n", n, k, mid);
  if(k >= mid){
    Room room;
    room.ld = 0; room.rd = 0;
    return room;
  } /*else if (k > mid/2){
      Room room;
      room.ld = 1; room.rd = 0;
      return room;
      }*/
  Room room;
  room.ld = 0; room.rd = 0;
  std::vector<int> v;
  std::priority_queue<int, std::vector<int>, std::less<int> >
    v2;
  v.push_back(n);
  v2.push(n);
  for(int i = 0; i < k; i++){
    /*int big = v[v.size()-1]-1;
    v[v.size()-1] = (big)/2;
    v.push_back((big+1)/2);
    
    if(i == k-1){
    room.ld = (big+1)/2;
      room.rd = big/2;
    }
    std::sort(v.begin()+v.size()-2, v.end());*/
    int big = v2.top()-1;
    v2.pop();
    v2.push((big+1)/2);
    v2.push((big)/2);
    if(i == k-1){
      room.ld = (big+1)/2;
      room.rd = big/2;
    }
  }
  return room;
}

int main(){
  int T, N, K;
  scanf("%d\n", &T);
  int t = 1;
  while(t < T+1){
    scanf("%d %d", &N, &K);
    Room room = getSideDistance2(N, K);
    printf("Case #%d: %d %d\n", t, room.ld, room.rd);
    t++;
    }
  /*int n = 180;
  for(int i = 1; i < n; i++){
    Room room = getSideDistance(n, i);
    fprintf(stderr, "%d, %d: %d %d\n", n, i, room.ld, room.rd);
    }*/
}
