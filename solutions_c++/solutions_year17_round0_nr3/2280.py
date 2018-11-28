#include <thread>
#include <mutex>
#include <condition_variable>
#include <atomic>
#include <chrono>
#include <iostream>
#include <fstream>
#include <exception>
#include <stdexcept> 
#include <string>
#include <sstream> 
#include <iomanip>
#include <algorithm> 

using namespace std;
using ccharp=const char *;
using charp=char *;

using xuint=unsigned __int64;
using xint=_int64;
using uint=unsigned int;
using byte=unsigned char *;


string file_path(ccharp path_in, ccharp name_in) {
  string to;
  to=path_in;
  to+=name_in;
  return to;
}

// error reporting in stream
class mifstream : public std::ifstream {
public:
  mifstream(ccharp path_in, ccharp name_in) {
    string pathname=file_path(path_in, name_in);
    open(pathname);
    if (!is_open()) {
      ostringstream err;
      err<<"can not open infile="<<pathname;
      throw err.str();
    }
    exceptions(ifstream::failbit|ifstream::badbit);
  }
  ~mifstream() {}
  int nextInt() { int res; *this>>res; return res; }
  string nextString() { string res; *this>>res; return res; }
  xint nextXInt() { xint res; *this>>res; return res; }
};

// error reporting out stream
class mofstream : public std::ofstream {
public:
  mofstream(ccharp path_in, ccharp name_in) {
    string pathname=file_path(path_in, name_in);
    open(pathname);
    if (!is_open()) {
      ostringstream err;
      err<<"can not open outfile="<<pathname;
      throw err.str();
    }
    exceptions(ifstream::failbit|ifstream::badbit);
  }
  ~mofstream() {}
};


// simple non dynamic array for speed and for simple debugging
template< typename T>
class vla {
public:
  vla(size_t sizeIn) { arrSize=0; maxSize=sizeIn; arr=new T[maxSize]; }
  vla(size_t sizeIn, const T &emptyIn) : vla(sizeIn) { all(emptyIn); }
  ~vla() { delete[] arr; }
  vla(vla const &)=delete;
  void operator=(vla const &)=delete;
  size_t size() { return arrSize; }
  size_t index(size_t i) { if (i>=arrSize) throw "vla::index"; return i; }
  T &operator[](size_t i) { return arr[index(i)]; }
  T operator[](size_t i) const { return arr[index(i)]; }
  void all(const T &v) { arrSize=maxSize; for (size_t i=0; i<arrSize; i++) arr[i]=v; }
  void dump() { for (size_t i=0; i<arrSize; i++) { cout<<i<<"="<<arr[i]<<endl; } }
  void dumpx() { for (size_t i=0; i<arrSize; i++) { cout<<i<<"="; arr[i].dump(cout); cout<<endl; } }
  void push_back(const T &v) { if (arrSize==maxSize) throw "vla::push_back"; arr[arrSize++]=v; }
  typedef T * iterator;
  typedef const T * const_iterator;
  iterator begin() { return arr; }
  iterator end() { return arr+arrSize; }
  T *at(size_t i) { return arr+index(i); }
private:
  T *arr;
  size_t arrSize;
  size_t maxSize;
};


// int main(int ac, char *av[]) { return mainx(ac, av, [](int i, mifstream &fi, mofstream &fo) { solve(i, fi, fo); }); }

int mainx(int ac, char *av[], std::function<void(int, mifstream &, mofstream &)> solveIn) {
  try {
    ccharp current_path=(1<ac) ? av[1] : ".";
    cout<<"current path="<<current_path<<endl;
    mifstream fi(current_path, "infile.txt");
    mofstream fo(current_path, "outfile.txt");
    int count=fi.nextInt();
    cout<<"number of tasks="<<count<<endl;
    for (int i=1; i<=count; i++) {
      cout<<"start "<<i<<endl;
      solveIn(i, fi, fo);
      cout<<"done "<<i<<endl;
    }
    cout<<"all done"<<endl;
    return 0;
  }
  catch (ifstream::failure e) {
    cout<<"exception opening/reading file "<<e.what()<<endl;
  }
  catch (const exception &e) {
    cout<<"exception="<<e.what()<<endl;
  }
  catch (ccharp s) {
    cout<<"exception="<<s<<endl;
  }
  catch (string s) {
    cout<<"exception="<<s<<endl;
  }
  catch (...) {
    cout<<"some exception"<<endl;
  }
  return 0;
}
