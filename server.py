import socket


def log(*args, **kwargs):
  print('log', *args, **kwargs)


def run(host='', port=3000):
  with socket.socket() as s:
    s.bind((host, port))
    
    while True:
      s.listen(5)
      connection, address = s.accept()
      request = connection.rect(1024)
      log('raw, ', request)
      request = request.decode('utf-8)
      log('ip, request, {}\n{}'.format(address, request))
      
      try:
        path = request.split()[1]
        response = response_for_path(path)
        connection.sendall(response)
      except Exception as e:
        log('error', e)

      connection.close()


def main():
  config = dict(
    host='',
    port=3000,
  )
  run(**config)


if __name__ = '__main__':
  main()
